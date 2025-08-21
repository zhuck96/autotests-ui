from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
     browser = playwright.chromium.launch(headless=False)
     context = browser.new_context()
     page = context.new_page()
     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
     email_login = page.get_by_test_id('login-form-email-input').locator('input')
     expect(email_login).to_be_visible()
     password_login = page.get_by_test_id('login-form-password-input').locator('input')
     expect(password_login).to_be_visible()
     login_login = page.get_by_test_id("login-page-login-button")
     expect(login_login).to_be_visible()
     registration = page.get_by_test_id("login-page-registration-link")
     registration.click()
     email_reg = page.get_by_test_id("registration-form-email-input").locator('input')
     expect(email_reg).to_be_visible()
     password_reg = page.get_by_test_id("registration-form-password-input").locator('input')
     expect(password_reg).to_be_visible()
     reg_button_on_reg_page = page.get_by_test_id("registration-page-registration-button")
     expect(reg_button_on_reg_page).to_be_visible()





