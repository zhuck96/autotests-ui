from playwright.sync_api import sync_playwright, expect

# работа с ошибками

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # unknown = page.locator("div.no_locator")
    # expect(unknown).to_be_visible()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Пытаемся изменить текст заголовка
    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """) # решается с помощью ожидания завершения сетевых запросов

