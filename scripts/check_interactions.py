"""Exercise real timers, focus, reduced motion, gallery and enquiries in Chromium."""
import argparse
import json
import shutil
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

def active(page):
    return page.locator('.carousel-item.active img').get_attribute('src')

def leave_slider(page):
    page.mouse.move(0, 0)
    page.evaluate('document.activeElement.blur()')

def advance(page):
    before = active(page)
    page.wait_for_timeout(5700)
    assert active(page) != before, ('autoplay did not advance', before)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    parser.add_argument('--output', default=str(ROOT / '.qa-output'))
    args = parser.parse_args()
    results = []
    errors = []
    with sync_playwright() as p:
        settings = {'headless':True, 'args':['--no-sandbox']}
        if shutil.which('chromium'):
            settings['executable_path'] = shutil.which('chromium')
        browser = p.chromium.launch(**settings)
        context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'])
        page = context.new_page()
        page.on('pageerror', lambda error:errors.append(str(error)))
        for width in [375, 768, 1440]:
            page.set_viewport_size({'width':width, 'height':1000})
            for name in ['destination.html', 'tour.html']:
                page.goto(args.base_url+'/'+name, wait_until='load')
                leave_slider(page)
                assert page.locator('.carousel-pause').count() == 0
                advance(page)
                before = active(page)
                page.get_by_role('button',name='Next photograph',exact=True).click()
                page.wait_for_timeout(700)
                assert before != active(page)
                leave_slider(page)
                advance(page)
                results.append(f'{name} {width}px: timed autoplay, next arrow and automatic resume')
                print(results[-1], flush=True)
        page.goto(args.base_url+'/destination.html', wait_until='load')
        page.locator('.carousel').hover()
        before = active(page)
        page.wait_for_timeout(5700)
        assert active(page) == before
        leave_slider(page)
        advance(page)
        page.get_by_role('button',name='Next photograph',exact=True).focus()
        before = active(page)
        page.wait_for_timeout(5700)
        assert active(page) == before
        page.keyboard.press('ArrowLeft')
        page.wait_for_timeout(700)
        assert active(page) != before
        leave_slider(page)
        advance(page)
        results.append('Hover/focus pause, left keyboard arrow, and resume after both interactions')
        for name in ['destination.html', 'tour.html']:
            page.emulate_media(reduced_motion='reduce')
            page.goto(args.base_url+'/'+name,wait_until='load')
            leave_slider(page)
            before = active(page)
            page.wait_for_timeout(5700)
            assert active(page) == before
            page.get_by_role('button',name='Next photograph',exact=True).click()
            page.wait_for_timeout(100)
            assert active(page) != before
            page.emulate_media(reduced_motion='no-preference')
            leave_slider(page)
            advance(page)
            results.append(name+': reduced motion blocks autoplay; manual control and live preference resume work')
        # Isolated single-slide fixture: no unnecessary controls or movement.
        page.goto(args.base_url+'/gallery.html',wait_until='load')
        page.evaluate("""() => {
          document.body.innerHTML='<div class="carousel"><div class="carousel-inner"><div class="carousel-item active">Only slide</div></div><div class="carousel-indicators"></div><button class="carousel-control-prev">Previous</button><button class="carousel-control-next">Next</button></div>';
        }""")
        page.add_script_tag(url=args.base_url+'/assets/js/carousels.js')
        assert not page.locator('.carousel-control-next').is_visible()
        results.append('Single-slide fixture hides redundant controls')
        page.set_viewport_size({'width':375,'height':812})
        page.goto(args.base_url+'/index.html',wait_until='load')
        page.get_by_role('button',name='Menu').click()
        assert page.get_by_role('navigation',name='Main navigation').is_visible()
        page.keyboard.press('Escape')
        assert page.get_by_role('button',name='Menu').get_attribute('aria-expanded')=='false'
        page.keyboard.press('Tab')
        page.goto(args.base_url+'/index.html',wait_until='load')
        page.keyboard.press('Tab')
        assert page.locator('.skip-link').evaluate('(link)=>link===document.activeElement')
        page.keyboard.press('Enter')
        assert page.locator('main').evaluate('(main)=>main===document.activeElement')
        results.append('Mobile menu, Escape key, and keyboard skip link')
        page.goto(args.base_url+'/gallery.html',wait_until='load')
        for label,count in [('Mountains',8),('Desert',8),('Sea side',8),('All photos',24)]:
            button=page.get_by_role('button',name=label,exact=True)
            button.focus();page.keyboard.press('Enter')
            assert page.locator('.photo-gallery figure:visible').count()==count
            assert button.get_attribute('aria-pressed')=='true'
        page.get_by_role('button',name='Desert',exact=True).click()
        opener=page.locator('.photo-gallery figure:visible .gallery-open').first
        opener.click()
        assert page.get_by_role('dialog',name='Photograph viewer').is_visible()
        before=page.locator('.lightbox-image').get_attribute('src')
        page.keyboard.press('ArrowRight')
        assert page.locator('.lightbox-image').get_attribute('src')!=before
        assert '/desert/' in page.locator('.lightbox-image').get_attribute('src')
        for _ in range(6):
            page.keyboard.press('Tab')
            assert page.evaluate('document.querySelector("dialog").contains(document.activeElement)')
        page.keyboard.press('Escape')
        assert not page.locator('dialog').is_visible()
        assert opener.evaluate('(link)=>link===document.activeElement')
        results.append('All gallery filters; category-scoped lightbox; keyboard arrows, focus containment and focus return')
        page.goto(args.base_url+'/culture.html',wait_until='load')
        page.locator('a[href="contact.html?tour=Heritage%20Walk"]').click()
        assert page.locator('#subject').input_value()=='Enquiry: Heritage Walk'
        assert not page.locator('form').evaluate('(form)=>form.checkValidity()')
        page.locator('#name').fill('QA Traveller');page.locator('#email').fill('invalid')
        page.locator('#message').fill('Please share details about this trip.')
        assert not page.locator('form').evaluate('(form)=>form.checkValidity()')
        page.locator('#email').fill('traveller@example.com')
        page.get_by_role('button',name='Prepare email').click()
        href=page.locator('#email-draft-link').get_attribute('href')
        query=parse_qs(urlsplit(href).query)
        assert query['subject']==['Enquiry: Heritage Walk'] and 'QA Traveller' in query['body'][0]
        page.get_by_role('button',name='Copy enquiry').click()
        page.wait_for_function('document.querySelector("#form-status").textContent.includes("Enquiry copied")')
        assert 'QA Traveller' in page.evaluate('navigator.clipboard.readText()')
        page.locator('#message').fill('Changed enquiry')
        assert page.locator('#email-draft-link').is_hidden()
        results.append('Enquiry subject, invalid/valid fields, encoded draft, clipboard and stale-draft reset')
        nojs=browser.new_context(java_script_enabled=False,viewport={'width':375,'height':812})
        q=nojs.new_page();q.goto(args.base_url+'/index.html')
        assert q.get_by_role('navigation',name='Main navigation').is_visible()
        q.goto(args.base_url+'/gallery.html')
        assert q.locator('.photo-gallery figure:visible').count()==24 and q.locator('.gallery-filters').is_hidden()
        q.goto(args.base_url+'/contact.html');assert q.locator('#copy-enquiry').is_hidden()
        results.append('No-JS navigation, full gallery/direct image links and direct-email fallback')
        browser.close()
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    (out/'interaction-results.json').write_text(json.dumps({'checks':results,'errors':errors},indent=2))
    assert not errors
    print('PASS:',len(results),'interaction groups; actual five-second timers were observed.',flush=True)


if __name__=='__main__':
    main()
