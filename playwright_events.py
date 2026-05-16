from playwright.sync_api import sync_playwright, expect, Request, Response


def log_requests(request: Request) -> None:
    print(f"Request: {request.url}")


def log_responses(response: Response) -> None:
    print(f"Response: {response.url}")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.on("request", log_requests)
    page.on("response", log_responses)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    page.wait_for_timeout(5000)
