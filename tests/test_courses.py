from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    no_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_text).to_be_visible()
    expect(no_text).to_have_text("There is no results")

    no_results_text = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(no_results_text).to_be_visible()
    expect(no_results_text).to_have_text("Results from the load test pipeline will be displayed here")
