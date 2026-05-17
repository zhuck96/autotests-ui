import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()


@pytest.fixture
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_field = page.get_by_test_id("registration-form-email-input").locator("input")
    email_field.fill("user.name@gmail.com")

    username_field = page.get_by_test_id("registration-form-username-input").locator("input")
    username_field.fill("username")

    password_field = page.get_by_test_id("registration-form-password-input").locator("input")
    password_field.fill("password")

    reg_button = page.get_by_role("button", name="Registration")
    reg_button.click()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()