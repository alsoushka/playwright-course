from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_title = page.locator("[data-test=\"title\"]")
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.error_message = page.locator("[data-test=\"error\"]")
        self.payment_info = page.locator("[data-test=\"payment-info-value\"]")
        self.shipping_info = page.locator("[data-test=\"shipping-info-value\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.thank_you_message = page.locator("[data-test=\"complete-header\"]")

        
   # Methods
    def fill_out_form(self):
       self.first_name.fill("Ambm")
       self.last_name.fill("jbjh")
       self.postal_code.fill("450044")
       self.continue_button.click()
       return self
    
    def click_finish(self):
       self.finish_button.click()
       return self
    
    
    # Getters
    def get_page_title(self):
        return self.page_title
    
    def get_continue_button(self):
        return self.continue_button
    
    def get_error_message(self):
        return self.error_message
    
    def get_payment_info(self):
       return self.payment_info
    
    def get_shipping_info(self):
       return self.shipping_info
    
    def get_thank_you_message(self):
       return self.thank_you_message
    

        
        
        
       