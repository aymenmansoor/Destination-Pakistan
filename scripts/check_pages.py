"""Run every route at every requested width; record headings and screenshots."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from playwright.sync_api import sync_playwright
import shutil

ROOT = Path(__file__).resolve().parents[1]
WIDTHS = [320, 375, 390, 576, 768, 991, 1024, 1440, 1920]
REPRESENTATIVE = ['index.html', 'destination.html', 'tour.html', 'Fairy.html',
                  'gallery.html', 'about.html', 'culture.html', 'contact.html', 'Mushkpuri.html', 'khunjerab.html', 'treking.html']

class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def static_checks():
    checks = 0
    for path in sorted(ROOT.glob('*.html')):
        parser = Inventory()
        parser.feed(path.read_text())
        ids = [attrs['id'] for _, attrs in parser.elements if 'id' in attrs]
        assert len(ids) == len(set(ids)), (path.name, 'duplicate IDs')
        for tag in ['main', 'h1']:
            assert sum(t == tag for t, _ in parser.elements) == 1, (path.name, tag)
        for _, attrs in parser.elements:
            for key in ['href', 'src']:
                if key not in attrs:
                    continue
                reference = urlsplit(attrs[key])
                if reference.scheme or reference.netloc:
                    continue
                target = ROOT / unquote(reference.path) if reference.path else path
                assert target.is_file(), (path.name, attrs[key])
                if reference.fragment:
                    target_parser = Inventory()
                    target_parser.feed(target.read_text())
                    assert any(a.get('id') == reference.fragment for _, a in target_parser.elements)
                checks += 1
    return checks


METRICS = """() => {
  const headings = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => {
    const range = document.createRange(); range.selectNodeContents(h);
    const lines = new Set([...range.getClientRects()].filter(r=>r.height>1).map(r=>Math.round(r.y)));
    return {text:h.textContent.trim(), tag:h.tagName, lines:lines.size,
      clipped:h.scrollWidth>h.clientWidth+1, font:getComputedStyle(h).fontSize};
  });
  const frame = document.querySelector('.guide-visual');
  const guide = frame ? (()=>{ const image=frame.querySelector('img'); const a=frame.getBoundingClientRect(), b=image.getBoundingClientRect(); return {width:a.width,height:a.height,imageWidth:b.width,imageHeight:b.height,background:getComputedStyle(frame).backgroundColor,fit:getComputedStyle(image).objectFit,titleBeforeImage:document.querySelector('h1').getBoundingClientRect().bottom <= a.top}; })():null;
  const nav = document.querySelector('.nav-inner').getBoundingClientRect();
  const footer = document.querySelector('footer').getBoundingClientRect();
  return {overflow:document.documentElement.scrollWidth-innerWidth,
    broken:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),
    distorted:[...document.images].filter(i=>i.clientWidth&&i.clientHeight&&getComputedStyle(i).objectFit==='fill'&&Math.abs(i.clientWidth/i.clientHeight-i.naturalWidth/i.naturalHeight)>.03).map(i=>i.src),
    headings, guide, navHeight:nav.height, footerWidth:footer.width,
    group:document.querySelector('.feature-image') ? {
      width:document.querySelector('.feature-image').clientWidth,
      height:document.querySelector('.feature-image').clientHeight,
      fit:getComputedStyle(document.querySelector('.feature-image')).objectFit
    }:null};
}"""


def main():
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--base-url', default='http://127.0.0.1:8000')
    arguments.add_argument('--output', default=str(ROOT / '.qa-output'))
    args = arguments.parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    print('Static references checked:', static_checks(), flush=True)
    results, failures, errors, http_errors = [], [], [], []
    with sync_playwright() as playwright:
        settings = {'headless': True, 'args': ['--no-sandbox']}
        if shutil.which('chromium'):
            settings['executable_path'] = shutil.which('chromium')
        browser = playwright.chromium.launch(**settings)
        page = browser.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
        page.on('response', lambda response: http_errors.append([response.url, response.status]) if response.status >= 400 else None)
        for width in WIDTHS:
            page.set_viewport_size({'width': width, 'height': 1000 if width >= 768 else 812})
            for path in sorted(ROOT.glob('*.html')):
                page.goto(args.base_url + '/' + quote(path.name), wait_until='load')
                page.mouse.move(0, 0)
                page.evaluate("""async () => {
                  await Promise.all([...document.images].map(img => {
                    img.loading='eager'; return img.decode().catch(()=>{});
                  }));
                }""")
                metrics = page.evaluate(METRICS)
                result = {'page': path.name, 'width': width, **metrics}
                results.append(result)
                guide=metrics['guide']
                if guide and (abs(guide['width']-guide['imageWidth'])>1 or abs(guide['height']-guide['imageHeight'])>1 or guide['background']!='rgba(0, 0, 0, 0)' or not guide['titleBeforeImage']):
                    failures.append({'page':path.name,'width':width,'reason':'guide frame bands or title placement','guide':guide})
                if metrics['overflow'] > 1 or metrics['broken'] or metrics['distorted'] or any(h['clipped'] for h in metrics['headings']):
                    failures.append(result)
                if width >= 1440 and path.name not in ['index.html', 'front.html']:
                    if metrics['headings'][0]['lines'] > 1:
                        failures.append({'page':path.name,'width':width,'reason':'avoidable desktop h1 wrapping'})
                page.locator('footer').scroll_into_view_if_needed()
                assert page.locator('footer').is_visible()
                if width in [375, 768, 1440]:
                    page.evaluate("document.activeElement.blur();window.scrollTo({top:0,behavior:'instant'})")
                    (output/'viewport').mkdir(exist_ok=True)
                    page.screenshot(path=str(output/'viewport'/f'{path.stem}-{width}.png'), animations='disabled')
                    if path.name in REPRESENTATIVE:
                        page.screenshot(path=str(output/f'{path.stem}-{width}.png'), full_page=True, animations='disabled')
            print(f'Rendered all 28 pages at {width}px', flush=True)
        landscape = []
        page.set_viewport_size({'width':1024,'height':768})
        for path in sorted(ROOT.glob('*.html')):
            page.goto(args.base_url+'/'+quote(path.name),wait_until='load')
            geometry=page.evaluate("() => ({overflow:document.documentElement.scrollWidth-innerWidth,clipped:[...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].some(h=>h.scrollWidth>h.clientWidth+1)})")
            landscape.append({'page':path.name,**geometry})
            if geometry['overflow']>1 or geometry['clipped']:
                failures.append(landscape[-1])
        # A 1920px desktop at 200% zoom has a 960px CSS layout viewport.
        page.set_viewport_size({'width': 960, 'height': 600})
        zoom = []
        for path in sorted(ROOT.glob('*.html')):
            page.goto(args.base_url + '/' + quote(path.name), wait_until='load')
            overflow = page.evaluate('document.documentElement.scrollWidth-innerWidth')
            zoom.append({'page':path.name,'overflow':overflow})
            if overflow > 1:
                failures.append(zoom[-1])
        # True text enlargement catches fixed heights and tight containers separately.
        page.set_viewport_size({'width': 1024, 'height': 768})
        for name in REPRESENTATIVE:
            page.goto(args.base_url + '/' + name, wait_until='load')
            page.add_style_tag(content='html { font-size: 200%; }')
            if page.evaluate('document.documentElement.scrollWidth-innerWidth') > 1:
                failures.append({'page':name,'reason':'200% text enlargement overflow'})
        browser.close()
    report = {'cases':len(results),'widths':WIDTHS,'results':results,
              'landscape':landscape,'zoom_reflow':zoom,'failures':failures,'javascript_errors':errors,'http_errors':http_errors}
    (output / 'page-results.json').write_text(json.dumps(report, indent=2))
    print('Failures:', json.dumps(failures), flush=True)
    print('JavaScript/console errors:', errors, 'HTTP errors:', http_errors, flush=True)
    assert not failures and not errors and not http_errors
    print('PASS: 252 route/viewport cases, all headings inspected, images loaded, footers reachable.', flush=True)


if __name__ == '__main__':
    main()
