from playwright.sync_api import sync_playwright
import time

def update_godaddy_dns():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()

        # Step 1: Go to GoDaddy login
        print("[1/6] Opening GoDaddy login...")
        page.goto("https://sso.godaddy.com/?realm=idp&app=dcc&path=%2Fmanage%2Focslakeorion.com%2Fdns")
        time.sleep(4)

        # Click "Use email" link first
        try:
            use_email = page.locator('a:has-text("Use email"), a:has-text("use email")').first
            use_email.click()
            time.sleep(2)
        except:
            pass

        # Try filling email
        try:
            email_field = page.locator('input[type="email"], input[id="username"], input[name="username"]').first
            email_field.fill("oaklandcleaningserviceslo@gmail.com")
            time.sleep(1)
        except:
            pass

        # Try password
        try:
            password_field = page.locator('input[type="password"], input[id="password"]').first
            password_field.fill("OCS0663!")
            time.sleep(1)
        except:
            pass

        # Click Sign In
        try:
            sign_in = page.locator('button:has-text("Sign In"), button[type="submit"]').first
            sign_in.click()
            time.sleep(10)
        except:
            pass

        # Screenshot after login attempt
        page.screenshot(path="C:/Users/Oakla/Desktop/OCS Website/dns_step2.png")
        print("[2/6] Login attempted. Checking page state...")

        current_url = page.url
        print(f"  Current URL: {current_url}")

        # If we're on the DNS page, proceed
        if "dns" not in current_url.lower():
            print("  Navigating to DNS page...")
            page.goto("https://dcc.godaddy.com/manage/ocslakeorion.com/dns")
            time.sleep(8)

        page.screenshot(path="C:/Users/Oakla/Desktop/OCS Website/dns_step3.png")
        print("[3/6] DNS page screenshot saved.")

        # Keep browser open for 120 seconds so user can see
        print("  Browser will stay open for 2 minutes...")
        time.sleep(120)
        browser.close()

if __name__ == "__main__":
    update_godaddy_dns()
