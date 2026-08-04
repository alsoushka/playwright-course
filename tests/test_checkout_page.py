from playwright.sync_api import Page
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage

# Click Finish
# Assert the message

def test_fill_out_page_is_visible(inventory_page: InventoryPage):
    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()
    assert checkout_page.get_page_title().text_content() == "Checkout: Your Information"

def test_all_information(inventory_page: InventoryPage):
    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()
    checkout_page.fill_out_form()
    assert checkout_page.get_payment_info().is_visible()
    assert checkout_page.get_shipping_info().is_visible()

def test_verify_thank_you_message(inventory_page: InventoryPage):
    cart_page = inventory_page.go_to_cart()
    checkout_page = cart_page.go_to_checkout()
    checkout_page.fill_out_form()
    checkout_page.click_finish()
    assert checkout_page.get_thank_you_message().text_content() == "Thank you for your order!"




