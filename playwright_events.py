from playwright.sync_api import sync_playwright,Request, Response

# работа с событиями - просмотр запросов отправляемых странцией и полученных кодов ответов по ним

# можно реализовать как отдельными функциями там и через lambda

# def log_request(request:Request):
#     print(f"Запрос {request.url}")
#
# def log_response(response:Response):
#     print(f"Ответ {response.url} {response.status}")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.on("request", log_request)
    # page.on("response", log_response)
    page.on("request",lambda request: print(request.url))
    page.on("response",lambda response: print(response.url, response.status))
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.wait_for_timeout(5000)