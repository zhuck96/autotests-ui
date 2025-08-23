from playwright.sync_api import sync_playwright, expect

# фокус на поле email и ввод через клавиатуру почты

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.focus()

    for char in "user@gmail.com":
        page.keyboard.press(key=char, delay=1000)

    page.keyboard.press(key="ControlOrMeta+A")
    page.wait_for_timeout(5000)
