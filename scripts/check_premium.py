"""Observe repeated autoplay, touch recovery, photograph layouts and motion."""
import argparse
import json
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    parser.add_argument('--output', default=str(ROOT / '.qa-output'))
    args = parser.parse_args()
    checks = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
        for width, touch in [(390, True), (768, False), (1440, False)]:
            context = browser.new_context(viewport={'width':width,'height':1000}, has_touch=touch, is_mobile=touch)
            page = context.new_page()
            for name in ['tour.html','destination.html']:
                page.goto(args.base_url+'/'+name, wait_until='load')
                page.evaluate('''() => {
                  window.transitions=[];
                  document.querySelector('.carousel').addEventListener('slid.bs.carousel', e => transitions.push(e.to));
                }''')
                image = page.locator('.carousel-item.active img')
                if touch:
                    image.tap()
                else:
                    image.hover()
                page.wait_for_function("transitions.length >= 3", timeout=24000)
                transitions = page.evaluate('transitions')
                assert len(transitions)==3, (name,width,'passive viewing stalled',transitions)
                assert len(set(transitions))==3, (name,width,transitions)
                next_button = page.get_by_role('button',name='Next photograph',exact=True)
                if touch:
                    next_button.tap()
                else:
                    next_button.click()
                    page.mouse.move(0,0)
                    page.evaluate('document.activeElement.blur()')
                page.wait_for_timeout(800)
                before=page.evaluate('transitions.length')
                page.wait_for_function("(before) => transitions.length >= before + 2", arg=before, timeout=16000)
                after=page.evaluate('transitions.length')
                assert after-before==2,(name,width,'manual navigation stopped autoplay',before,after)
                checks.append({'page':name,'width':width,'touch':touch,'initial_transitions':transitions,'resumed_transitions':after-before})
                print(checks[-1],flush=True)
            page.goto(args.base_url+'/index.html')
            sizes=page.locator('.mini-gallery img').evaluate_all('(images)=>images.map(i=>Math.round(i.getBoundingClientRect().height))')
            assert max(sizes)-min(sizes)<=1, (width,sizes)
            checks.append({'gallery_width':width,'heights':sizes})
            context.close()
        page=browser.new_page(viewport={'width':1440,'height':1000})
        page.goto(args.base_url+'/tour.html')
        page.mouse.move(0,0)
        page.evaluate('window.count=0;document.querySelector(".carousel").addEventListener("slid.bs.carousel",()=>count++)')
        page.add_script_tag(url=args.base_url+'/assets/js/carousels.js')
        page.wait_for_function('count >= 2', timeout=16000)
        page.wait_for_timeout(500)
        assert page.evaluate('count')==2
        checks.append('Repeated initialization: exactly two transitions across two intervals')
        page.goto(args.base_url+'/contact.html')
        active=page.locator('.nav-contact[aria-current="page"]')
        assert active.evaluate('e=>getComputedStyle(e,"::after").content')=='none'
        assert '+1234567890' not in page.locator('body').inner_text()
        page.goto(args.base_url+'/gallery.html')
        assert page.locator('.gallery-count').count()==0
        page.get_by_role('button',name='Desert',exact=True).click()
        assert page.locator('.photo-gallery figure:visible').count()==8
        assert page.locator('.filter-arriving').first.evaluate('e=>getComputedStyle(e).animationName')=='photograph-arrival'
        page.wait_for_timeout(500)
        assert page.locator('.filter-arriving').count()==0
        page.goto(args.base_url+'/index.html')
        page.evaluate("window.started=[];document.addEventListener('animationstart', e=>started.push(e.animationName))")
        page.evaluate("window.scrollTo({top:document.querySelectorAll('.home .section-heading')[1].getBoundingClientRect().top+scrollY-120,behavior:'instant'})")
        page.wait_for_function("started.includes('section-arrival')")
        page.wait_for_timeout(700)
        assert page.locator('.is-arriving').count()==0
        checks.append('Equal-height homepage triptych, single Contact active indicator, no public placeholder phone/count, and completed reveal/filter animations')
        page.emulate_media(reduced_motion='reduce')
        page.goto(args.base_url+'/gallery.html')
        page.get_by_role('button',name='Desert',exact=True).click()
        assert page.locator('.filter-arriving').count()==0
        assert page.locator('.gallery-open img').first.evaluate('e=>getComputedStyle(e).transitionDuration')=='0s'
        checks.append('Reduced motion suppresses reveal/filter/hover animations')
        browser.close()
    output=Path(args.output);output.mkdir(parents=True,exist_ok=True)
    (output/'premium-results.json').write_text(json.dumps(checks,indent=2))
    print('PASS:',len(checks),'premium checks',flush=True)

if __name__=='__main__':
    main()
