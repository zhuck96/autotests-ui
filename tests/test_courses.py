import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
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
        context.storage_state(path='result_auth_storage.json')

        context_new = browser.new_context(storage_state='result_auth_storage.json')
        page_new = context_new.new_page()
        page_new.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page_new.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        no_results = page_new.get_by_test_id("courses-list-empty-view-title-text")
        expect(no_results).to_be_visible()
        expect(no_results).to_have_text("There is no results")

        icon = page_new.get_by_test_id("courses-list-empty-view-icon")
        expect(icon).to_be_visible()

        results_from = page_new.get_by_test_id("courses-list-empty-view-description-text")
        expect(results_from).to_be_visible()
        expect(results_from).to_have_text("Results from the load test pipeline will be displayed here")
