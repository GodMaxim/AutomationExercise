from playwright.sync_api import expect

class CheckoutPage:
    def __init__(self,page):
        self.page = page
        self.info = page.locator('div[data-qa="checkout-info"]')
        self.description_area = page.locator('#ordermsg textarea.form-control')
        self.place_order = page.locator('a[href="/payment"]')
        self.address_info = page.locator('#address_delivery')
        self.delete_account_btn = page.locator('a[href="/delete_account"]')
        self.deleted_account_title = page.locator('h2', has_text='Account Deleted')

    def check_info(self):
        expect(self.info).to_be_visible()

    def place_order_with_description(self):
        self.description_area.fill('Some description')
        self.place_order.click()  

    def check_address(self):
        expect(self.address_info).to_contain_text('Baker St.')  

    def click_on_delete_account(self):
            self.delete_account_btn.click()
        
    def check_deleted_account(self):
        expect(self.deleted_account_title).to_be_visible()
