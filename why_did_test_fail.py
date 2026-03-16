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

    # Output text of all items
    items = page.locator(".elig-select-main").all_inner_texts()
    print("Initial items:", items)

    # Click "Land" sector
    page.get_by_text("Land", exact=True).first.click()
    page.wait_for_timeout(500)

    items_after = page.locator(".elig-select-main").all_inner_texts()
    print("Items after clicking Land:", items_after)

    # Try to find geomatics
    try:
        page.get_by_text("Geomatics", exact=True).click()
        print("Clicked exact Geomatics!")
    except Exception as e:
        print("Failed to click exact Geomatics:", e)

    try:
        page.locator("text=Geomatics").click()
        print("Clicked text Geomatics!")
    except Exception as e:
        print("Failed to click text Geomatics:", e)

    page.screenshot(path="step1-pathways.png", full_page=True)
    browser.close()
