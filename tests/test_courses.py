from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
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

    with sync_playwright() as playwright_new:
        new_browser = playwright_new.chromium.launch(headless=False)
        context_with_auth = new_browser.new_context(storage_state="browser-state.json")
        new_page = context_with_auth.new_page()
        new_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_title = new_page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        icon = new_page.get_by_test_id("courses-list-empty-view-icon")
        expect(icon).to_be_visible()

        no_text = new_page.get_by_test_id("courses-list-empty-view-title-text")
        expect(no_text).to_be_visible()
        expect(no_text).to_have_text("There is no results")

        no_results_text = new_page.get_by_test_id("courses-list-empty-view-description-text")
        expect(no_results_text).to_be_visible()
        expect(no_results_text).to_have_text("Results from the load test pipeline will be displayed here")
