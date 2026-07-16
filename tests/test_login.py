import re
from playwright.sync_api import Page, expect


def test_example1(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"secondary-header\"]")).to_be_visible()

import re
from playwright.sync_api import Page, expect

def test_example2(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_example3(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()

