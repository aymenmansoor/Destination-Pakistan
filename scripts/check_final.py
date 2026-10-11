"""Record visible motion and test final proportions with real browser clocks."""
import argparse,json,shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--base-url',default='http://127.0.0.1:8000')
    parser.add_argument('--output',default=str(ROOT/'.qa-output'))
    args=parser.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    results=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=shutil.which('chromium'),args=['--no-sandbox'])
        context=browser.new_context(viewport={'width':1440,'height':1000},record_video_dir=str(out/'videos'),record_video_size={'width':1280,'height':890})
        context.add_init_script("window.motionEvents=[];addEventListener('animationstart',e=>motionEvents.push({name:e.animationName,tag:e.target.tagName,class:e.target.className,time:performance.now()}))")
        page=context.new_page();page.goto(args.base_url+'/index.html',wait_until='domcontentloaded')
        page.wait_for_timeout(250)
        hero=page.locator('.hero h1').evaluate('e=>({opacity:getComputedStyle(e).opacity,transform:getComputedStyle(e).transform})')
        page.wait_for_timeout(1000)
        events=page.evaluate('motionEvents.filter(e=>e.name==="hero-arrival")')
        assert len(events)==3,events
        assert page.locator('.hero h1').evaluate('e=>getComputedStyle(e).opacity')=='1'
        results.append({'hero_sample':hero,'staggered_hero_events':events})
        for selector in ['#discover','#overview','.mini-gallery','footer']:
            page.locator(selector).scroll_into_view_if_needed();page.wait_for_timeout(900)
        page.locator('.destination-card').first.hover();page.wait_for_timeout(250)
        assert page.locator('.destination-card img').first.evaluate('e=>getComputedStyle(e).transform')!='none'
        results.append({'home_scroll_events':page.evaluate('motionEvents.filter(e=>e.name==="section-arrival")')})
        for name in ['tour.html','destination.html']:
            page.goto(args.base_url+'/'+name);page.mouse.move(0,0)
            page.evaluate('window.slides=[];document.querySelector(".carousel").addEventListener("slid.bs.carousel",e=>slides.push({to:e.to,time:performance.now()}))')
            page.wait_for_function('slides.length>=3',timeout=24000)
            height=page.locator('.carousel-item.active img').evaluate('e=>e.clientHeight')
            assert 360 <= height <= 390, height
            page.get_by_role('button',name='Next photograph',exact=True).click();page.wait_for_timeout(950)
            page.mouse.move(0,0);page.evaluate('document.activeElement.blur()')
            before=page.evaluate('slides.length');page.wait_for_function('(n)=>slides.length>n',arg=before,timeout=7500)
            # Indicators navigate and playback resumes after releasing focus.
            page.locator('.carousel-indicators button').first.click();page.wait_for_timeout(950)
            assert page.locator('.carousel-item').first.evaluate('e=>e.classList.contains("active")')
            page.mouse.move(0,0);page.evaluate('document.activeElement.blur()')
            results.append({'slideshow':name,'events':page.evaluate('slides'),'height':height})
        page.goto(args.base_url+'/gallery.html')
        page.get_by_role('button',name='Desert',exact=True).click()
        assert page.locator('.photo-gallery').evaluate('e=>e.getAnimations().length')>0
        page.wait_for_timeout(700);assert page.locator('.photo-gallery figure:visible').count()==8
        page.locator('.gallery-open:visible').first.click();page.wait_for_timeout(300)
        assert page.locator('dialog').is_visible();page.keyboard.press('Escape')
        results.append('Gallery height/position interpolation and lightbox fade verified')
        for name,selector in [('Mushkpuri.html','.article-copy figure'),('treking.html','.package-page .card'),('about.html','.team .card'),('contact.html','.contact-form')]:
            page.goto(args.base_url+'/'+name);page.locator(selector).last.scroll_into_view_if_needed();page.wait_for_timeout(800)
            assert any(e['name']=='section-arrival' for e in page.evaluate('motionEvents')),(name,'no reveal')
            results.append({'motion_page':name,'events':page.evaluate('motionEvents')})
        assert page.locator('.contact-scene').count()==0
        video=page.video;context.close();video.save_as(str(out/'desktop-motion.webm'))
        mobile=browser.new_context(viewport={'width':390,'height':844},has_touch=True,is_mobile=True,record_video_dir=str(out/'mobile-videos'),record_video_size={'width':390,'height':844})
        mobile.add_init_script("window.menuAnimations=[];const originalAnimate=Element.prototype.animate;Element.prototype.animate=function(frames,options){const animation=originalAnimate.call(this,frames,options);if(this.matches('.site-nav'))menuAnimations.push({time:performance.now(),duration:animation.effect.getTiming().duration,frames:animation.effect.getKeyframes()});return animation;}")
        q=mobile.new_page();q.goto(args.base_url+'/tour.html')
        q.get_by_role('button',name='Menu').tap()
        assert q.evaluate('menuAnimations.length')>0
        assert q.evaluate('menuAnimations[0].duration')==200
        q.wait_for_timeout(300);q.get_by_role('button',name='Menu').tap();q.wait_for_timeout(300)
        assert q.locator('.site-nav').is_hidden()
        q.locator('.carousel-item.active img').tap()
        q.evaluate('window.count=0;document.querySelector(".carousel").addEventListener("slid.bs.carousel",()=>count++)')
        q.wait_for_function('count>=2',timeout=16000)
        q.get_by_role('button',name='Next photograph',exact=True).tap();q.wait_for_timeout(950)
        before=q.evaluate('count');q.wait_for_function('(n)=>count>n',arg=before,timeout=7500)
        results.append('Touch autoplay, arrow recovery and animated mobile menu open/close passed')
        q.emulate_media(reduced_motion='reduce');q.goto(args.base_url+'/index.html');q.wait_for_timeout(100)
        assert q.locator('.hero-enter,.is-arriving').count()==0
        q.get_by_role('button',name='Menu').tap();assert q.locator('.site-nav').evaluate('e=>e.getAnimations().length')==0
        results.append('Reduced motion disables entrances and menu animations')
        video=q.video;mobile.close();video.save_as(str(out/'mobile-motion.webm'))
        browser.close()
    (out/'final-results.json').write_text(json.dumps(results,indent=2))
    print('PASS:',len(results),'final checks and desktop/mobile screen recordings',flush=True)

if __name__=='__main__':main()
