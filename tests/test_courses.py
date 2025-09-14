import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    no_results = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results).to_be_visible()
    expect(no_results).to_have_text("There is no results")

    icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    results_from = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(results_from).to_be_visible()
    expect(results_from).to_have_text("Results from the load test pipeline will be displayed here")
