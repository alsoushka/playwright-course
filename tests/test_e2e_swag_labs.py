import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)

def test_checkout_happy_path(page: Page, username: str, password: str) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("John")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("Smith")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("94300")
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"payment-info-label\"]")).to_contain_text("Payment Information:")
    expect(page.locator("[data-test=\"shipping-info-label\"]")).to_contain_text("Shipping Information:")
    expect(page.locator("[data-test=\"total-info-label\"]")).to_contain_text("Price Total")
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"generate-pdf-order\"]")).to_be_visible()
