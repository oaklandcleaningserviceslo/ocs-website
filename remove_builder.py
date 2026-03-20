from playwright.sync_api import sync_playwright
import time

def remove_website_builder():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=400)
        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()

        # Step 1: Login
        print("[1] Logging into GoDaddy...")
        page.goto("https://sso.godaddy.com/?realm=idp&app=dcc&path=%2F")
        time.sleep(4)

        # Click "Use email"
        try:
            page.locator('a:has-text("Use email")').first.click()
            time.sleep(2)
        except:
            pass

        # Fill email
        try:
            page.locator('input[type="email"], input[id="username"], input[name="username"]').first.fill("oaklandcleaningserviceslo@gmail.com")
            time.sleep(1)
        except:
            pass

        # Fill password
        try:
            page.locator('input[type="password"], input[id="password"]').first.fill("OCS0663!")
            time.sleep(1)
        except:
            pass

        # Click Sign In
        try:
            page.locator('button:has-text("Sign In"), button[type="submit"]').first.click()
        except:
            pass

        time.sleep(10)
        page.screenshot(path="C:/Users/Oakla/Desktop/OCS Website/step1_login.png")
        print(f"  URL after login: {page.url}")

        # Step 2: Go to products
        print("[2] Navigating to products page...")
        page.goto("https://account.godaddy.com/products")
        time.sleep(8)
        page.screenshot(path="C:/Users/Oakla/Desktop/OCS Website/step2_products.png")
        print(f"  URL: {page.url}")

        # Step 3: Try to find Website Builder section and manage/cancel
        print("[3] Looking for Website Builder...")

        # Scroll down to find it
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        page.screenshot(path="C:/Users/Oakla/Desktop/OCS Website/step3_scrolled.png")

        # Try clicking on Websites + Marketing or Website Builder
        found = False
        for text in ["Manage", "Website Builder", "Websites + Marketing", "Websites"]:
            try:
                el = page.locator(f'a:has-text("{text}"), button:has-text("{text}")').first
                if el.is_visible(timeout=3000):
                    print(f"  Found: {text}")
                    el.click()
                    time.sleep(5)
                    found = True
                    break
            except:
                continue

        page.screenshot(path="C:/Users/Oakla/Desktop/OCS Website/step4_builder.png")
        print(f"  URL: {page.url}")

        # Keep browser open
        print("[4] Keeping browser open for 180 seconds...")
        print("  Screenshots saved to OCS Website folder.")
        time.sleep(180)
        browser.close()

if __name__ == "__main__":
    remove_website_builder()
