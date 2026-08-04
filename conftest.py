import pytest
from playwright.sync_api import Page

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture for login page"""
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def inventory_page(login_page: LoginPage) -> InventoryPage:
    return login_page.login_standard_user()