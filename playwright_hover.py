from playwright.sync_api import sync_playwright

# наведение курсора на элемент

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    registration_button = page.get_by_test_id("login-page-registration-link")
    registration_button.hover()

    page.wait_for_timeout(5000)
