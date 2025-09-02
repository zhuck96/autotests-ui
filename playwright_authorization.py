from playwright.sync_api import sync_playwright, expect

# работа с формой логина а затем переход на форму регистрации

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")


    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")


    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("password")


    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()


    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")


