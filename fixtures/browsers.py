import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=850)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.focus()
    email_input.fill("email@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.focus()
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.focus()
    password_input.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()
    context.storage_state(path='browser-state.json')


