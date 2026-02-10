from playwright.sync_api import sync_playwright
from .parser import FindInfo
def getTools(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        findInfo = FindInfo()

        page.goto('https://brain.com.ua/')
        page.locator("//div[@class='header-bottom']//input[@class='quick-search-input']").click()
        page.type('input', 'Apple iPhone 15 128GB Black')
        page.keyboard.press('Enter')
        page.wait_for_load_state(timeout=70000)
        page.locator("//div[@class='row']//div[@data-pid='1044347']//div[@class='br-pp-imadds']//img").click()
        page.wait_for_load_state(timeout=70000)

        return findInfo.find(page)


