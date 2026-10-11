"""Check entrances on every guide/category and rapid/reduced-motion UI changes."""
import json,shutil,argparse
from pathlib import Path
from urllib.parse import quote
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--base-url',default='http://127.0.0.1:8000');parser.add_argument('--output',default=str(ROOT/'.qa-output'));args=parser.parse_args();results=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=shutil.which('chromium'),args=['--no-sandbox']);context=browser.new_context(viewport={'width':1440,'height':1000})
        context.add_init_script("window.events=[];addEventListener('animationstart',e=>events.push({name:e.animationName,tag:e.target.tagName,class:e.target.className}))")
        page=context.new_page()
        for path in sorted(ROOT.glob('*.html')):
            source=path.read_text()
            if 'destination-guide' not in source and 'package-page' not in source:continue
            page.goto(args.base_url+'/'+quote(path.name));page.wait_for_timeout(150)
            if 'destination-guide' in source:
                page.locator('.article-copy > p').first.scroll_into_view_if_needed();page.wait_for_timeout(150)
                events=page.evaluate('events');assert any(e['tag']=='H1' for e in events),path.name
                assert any(e['tag']=='P' for e in events),path.name
                assert page.locator('.guide-visual').evaluate('e=>e.getAnimations().length')==0
            else:
                page.locator('.package-page .card').last.scroll_into_view_if_needed();page.wait_for_timeout(150)
                events=page.evaluate('events');assert any('card' in e['class'] for e in events),path.name
            results.append({'page':path.name,'events':events})
        page.goto(args.base_url+'/gallery.html')
        for label in ['Desert','Mountains','Sea side','All photos']:
            page.get_by_role('button',name=label,exact=True).click()
        page.wait_for_timeout(500)
        assert page.locator('.photo-gallery figure:visible').count()==24
        assert page.locator('.photo-gallery').evaluate('e=>e.getAnimations().length')==0
        results.append('Rapid gallery filters end with all images and no stale grid animation')
        page.set_viewport_size({'width':390,'height':844});page.goto(args.base_url+'/index.html')
        page.get_by_role('button',name='Menu').click();page.emulate_media(reduced_motion='reduce')
        page.wait_for_timeout(50)
        assert page.locator('.site-nav').is_visible() and page.locator('.site-nav').evaluate('e=>e.getAnimations().length')==0
        page.get_by_role('button',name='Menu').click();assert page.locator('.site-nav').is_hidden()
        results.append('Live reduced-motion preference cancels menu animation without losing open/closed state')
        browser.close()
    output=Path(args.output);output.mkdir(parents=True,exist_ok=True);(output/'motion-pages-results.json').write_text(json.dumps(results,indent=2));print('PASS: 21 guide/category animation checks and 2 rapid/preference-change checks',flush=True)

if __name__=='__main__':main()
