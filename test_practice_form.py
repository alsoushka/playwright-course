import re
from playwright.sync_api import Page, expect


def test_practice_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("hgvxh")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("nhbx")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("hvngng@jhgs.com")
    page.get_by_role("radio", name="Male", exact=True).check()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("1234567890")
    page.get_by_text("Sports").click()
    # expect(page.get_by_role("checkbox", name="Sports")).to_be_visible()
    checkbox = page.get_by_role("checkbox", name="Sports")
    assert checkbox.is_checked()
    
    page.locator("#uploadPicture").click()
    page.locator("#uploadPicture").set_input_files("/Users/alsououlmacheva/PythonPlaywright/playwright-course/test_data/580CC1F7-E973-44D3-830C-6F8B3D1702DB_Original.JPG")
    page.get_by_role("button", name="Submit").click()
    # expect(page.locator("#example-modal-sizes-title-lg")).to_contain_text("Thanks for submitting the form")
    actual_text = page.get_by_role("dialog", name="Thanks for submitting the form").text_content()
    expected_text = "Thanks for submitting the form"
    assert expected_text in actual_text