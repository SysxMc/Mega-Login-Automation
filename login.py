import time
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

MEGA_EMAIL = os.getenv("MEGA_EMAIL")
MEGA_PASSWORD = os.getenv("MEGA_PASSWORD")

def login_and_idle(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("🌐 Navigating to MEGA...")
        page.goto("https://mega.nz/login", timeout=60000)

        print("✍️ Entering credentials...")
        page.fill("#login-name2", MEGA_EMAIL)
        page.fill("#login-password2", MEGA_PASSWORD)
        page.press("#login-password2", "Enter")

        page.wait_for_url("**/fm/**", timeout=15000)
        print("✅ Login successful!")

        print("⏳ Idling for 30 minutes...")
        time.sleep(1800)

    except Exception as e:
        print(f"❌ Error during login or wait: {e}")
    finally:
        context.close()
        browser.close()
        print("🧹 Session cleaned up.")

if __name__ == "__main__":
    with sync_playwright() as playwright:
        while True:
            login_and_idle(playwright)
