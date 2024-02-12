from playwright.sync_api import sync_playwright

username = 'kalyan'
password = 'Test1234'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto('https://ad-emea-uat.pricefx.eu/app/modules/?partition=ad-emea-uat#/administration/useradmin')
    page.get_by_label("username").fill(username)
    page.get_by_label("password").fill(password)
    page.click('button[type=submit]')
    page.goto('https://ad-emea-uat.pricefx.eu/app/modules/?partition=ad-emea-uat#/administration/useradmin')
    page.get_by_role("button", name="Export").click()