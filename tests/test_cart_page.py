import pytest
from playwright.sync_api import Page

from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage


def test_cart_page_load(inventory_page: InventoryPage):
    cart_page = inventory_page.go_to_cart()

    # Verify title
    assert cart_page.get_page_title().text_content() == "Your Cart"
    # Verify checkout is visible
    assert cart_page.get_checkout_button().is_visible()

#  Parametrize later
def test_add_item_to_cart(inventory_page: InventoryPage):
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    
    cart_page = inventory_page.go_to_cart()

    #     assert the item count went up
    assert cart_page.get_item_count() == 1
    #     assert the item title is correct
    assert "Sauce Labs Backpack" in cart_page.get_item_name()
