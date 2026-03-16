from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 1024})

    import os
    filepath = f"file://{os.path.abspath('Charterly_RICS_Claude P02 (7).html')}"
    page.goto(filepath)

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)

    page.evaluate("S.body = 'RICS'; goStep(1)")
    page.wait_for_timeout(1000)

    # Click "Land" sector
    page.get_by_text("Land", exact=True).first.click()
    page.wait_for_timeout(500)

    page.screenshot(path="step1-pathways.png", full_page=True)

    # Check if Geomatics is there
    has_geo = page.locator("text=Geomatics").count() > 0
    print("Has Geomatics?", has_geo)

    browser.close()
