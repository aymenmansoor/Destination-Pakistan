"""Verify the requested shared proportions and capture every guide/category."""
import argparse, json, shutil, subprocess
from pathlib import Path
from urllib.parse import quote
from lxml import html
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    parser.add_argument('--output', default=str(ROOT / '.qa-output'))
    args = parser.parse_args()
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    guides, categories, results = [], [], []
    for path in sorted(ROOT.glob('*.html')):
        doc = html.fromstring(path.read_text())
        if doc.xpath('//body[@class="destination-guide"]'): guides.append(path)
        if doc.xpath('//body[@class="package-page"]'):
            categories.append(path)
            old = html.fromstring(subprocess.check_output(['git','show','HEAD:'+path.name], cwd=ROOT))
            text = lambda d: [' '.join(e.text_content().split()) for e in d.xpath('//article[@class="card"]')]
            assert text(doc) == text(old), (path.name, 'package information changed')
    assert len(guides) == 12 and len(categories) == 9
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
        page = browser.new_page()
        for width in [320,375,390,768,1024,1440,1920]:
            page.set_viewport_size({'width':width,'height':1000})
            for path in guides + categories:
                page.goto(args.base_url+'/'+quote(path.name), wait_until='load')
                page.evaluate("async()=>{await Promise.all([...document.images].map(i=>{i.loading='eager';return i.decode().catch(()=>{});}));}")
                if path in guides:
                    data = page.evaluate("""()=>{const frame=document.querySelector('.guide-visual'),image=frame.querySelector('img'),heading=document.querySelector('.page-heading'),sidebar=document.querySelector('.article-sidebar');return {width:frame.clientWidth,ratio:image.clientWidth/image.clientHeight,complete:frame.classList.contains('guide-visual-complete'),originalLink:frame.querySelector('a').getAttribute('href')===image.getAttribute('src'),background:getComputedStyle(heading).backgroundColor,label:heading.querySelector('.eyebrow').textContent.trim(),intro:heading.querySelector('p').textContent,columns:getComputedStyle(document.querySelector('.article-layout')).gridTemplateColumns.split(' ').length,sidebar:getComputedStyle(sidebar).backgroundColor};}""")
                    assert data['background']=='rgb(238, 233, 221)' and data['label']=='Destination guide', (path.name,data)
                    assert data['originalLink'] and not data['complete'], (path.name,data)
                    assert data['columns']==(2 if width>=768 else 1), (path.name,data)
                    assert data['sidebar']=='rgb(238, 226, 207)',(path.name,data)
                    if width>=1440:
                        assert 1000<=data['width']<=1050, (path.name,data)
                        if not data['complete']: assert 2.39<=data['ratio']<=2.8,(path.name,data)
                else:
                    assert page.locator('.page-heading').evaluate('e=>getComputedStyle(e).backgroundColor')=='rgb(238, 233, 221)'
                    assert page.locator('.page-heading .eyebrow').is_visible()
                    assert page.locator('.price-note').evaluate('e=>getComputedStyle(e).backgroundColor')=='rgb(238, 226, 207)'
                    data = page.evaluate("""()=>{const grid=document.querySelector('.row.g-4'),cards=[...grid.querySelectorAll('.card')];return {columns:getComputedStyle(grid).gridTemplateColumns.split(' ').length,heights:cards.map(c=>c.getBoundingClientRect().height),tops:cards.map(c=>Math.round(c.getBoundingClientRect().top)),images:cards.map(c=>c.querySelector('img').clientHeight),buttons:cards.map(c=>Math.round(c.querySelector('.btn').getBoundingClientRect().bottom))};}""")
                    assert data['columns']==(3 if width>=1200 else 2 if width>=768 else 1),(path.name,data)
                    assert all(190<=n<=210 for n in data['images']),(path.name,data)
                    for top in set(data['tops']):
                        indices=[i for i,t in enumerate(data['tops']) if t==top]
                        heights=[data['heights'][i] for i in indices]; bottoms=[data['buttons'][i] for i in indices]
                        assert max(heights)-min(heights)<=1 and max(bottoms)-min(bottoms)<=1,(path.name,data)
                results.append({'page':path.name,'width':width,**data})
                if width in [375,768,1440]:
                    page.wait_for_timeout(600)
                    page.screenshot(path=str(out/f'{path.stem}-{width}.png'),full_page=True,animations='disabled')
            for name in ['tour.html','destination.html']:
                page.goto(args.base_url+'/'+name)
                assert page.locator('.page-heading').evaluate('e=>getComputedStyle(e).backgroundColor')=='rgb(238, 233, 221)'
                assert page.locator('.page-heading .eyebrow').is_visible()
                data=page.evaluate("""()=>{const frame=document.querySelector('.cinema-band'),image=frame.querySelector('.carousel-item.active img'),next=frame.nextElementSibling;return {width:frame.clientWidth,height:image.clientHeight,radius:getComputedStyle(frame).borderRadius,gap:next.querySelector(".card").getBoundingClientRect().top-frame.getBoundingClientRect().bottom,caption:getComputedStyle(frame.querySelector('.slide-caption a')).fontSize};}""")
                assert data['radius']=='10px' and 25<=data['gap']<=35,(name,data)
                if width>=1440:assert data['width']==1050 and 360<=data['height']<=390 and 30<=float(data['caption'][:-2])<=34,(name,data)
                results.append({'page':name,'viewport':width,**data})
            page.goto(args.base_url+'/index.html')
            sizes=page.locator('.mini-gallery img').evaluate_all('(images)=>images.map(i=>i.clientHeight)')
            assert max(sizes)-min(sizes)<=1,(width,sizes)
            page.goto(args.base_url+'/contact.html')
            assert page.locator('.contact-scene').count()==0
            assert page.locator('.page-heading').evaluate('e=>getComputedStyle(e).backgroundColor')=='rgba(0, 0, 0, 0)'
            print('Shared guide/card/slider checks passed at',width,flush=True)
        page.goto(args.base_url+'/safarie.html');page.wait_for_timeout(700)
        card=page.locator('.card').first;card.hover();page.wait_for_timeout(300)
        hover=card.evaluate('e=>({transform:getComputedStyle(e).transform,shadow:getComputedStyle(e).boxShadow,image:getComputedStyle(e.querySelector("img")).transform})')
        assert hover['transform']!='none' and hover['image']!='none'
        page.emulate_media(reduced_motion='reduce');page.wait_for_timeout(100)
        assert card.evaluate('e=>getComputedStyle(e).transform')=='none'
        browser.close()
    (out/'design-results.json').write_text(json.dumps({'cases':len(results),'preserved_package_pages':len(categories),'hover':hover,'results':results},indent=2))
    print('PASS:',len(results),'design cases; unchanged package information; real hover/reduced-motion checks',flush=True)

if __name__=='__main__':main()
