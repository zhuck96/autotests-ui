from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    email = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input = "user.name@gmail.com"
    email.click()
    email.fill(email_input)

    username = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input = "username"
    username.click()
    username.fill(username_input)

    password = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input = "password"
    password.click()
    password.fill(password_input)

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")
