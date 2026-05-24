from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page, registration_page,dashboard_page):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form("email","username","12345")
    registration_page.reg_button.click()
    dashboard_page.check_dashboard_title()