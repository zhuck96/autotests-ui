from playwright.sync_api import sync_playwright, expect

# проверка локатора на наличие атрибута disabled


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_button = page.get_by_test_id("login-page-login-button")
    expect(login_button).to_be_disabled()
