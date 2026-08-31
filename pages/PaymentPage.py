from playwright.sync_api import expect

class PaymentPage:
    def __init__(self,page):
        self.page = page
        self.name_on_card = page.locator('input[data-qa="name-on-card"]')
        self.card_number = page.locator('input[data-qa="card-number"]')
        self.cvc = page.locator('input[data-qa="cvc"]')
        self.expiration = page.locator('input[data-qa="expiry-month"]')
        self.expiration_year = page.locator('input[data-qa="expiry-year"]')
        self.submit = page.locator('#submit')
        self.succsess_message = page.locator('#succsess_message')
        self.invoice_download_btn = page.locator('a[href*="/download_invoice/"]')
        self.continue_btn = page.locator('a[data-qa="continue-button"]')

    def fill_inputs(self):
        self.name_on_card.fill('John')
        self.card_number.fill('2323232323232323')
        self.cvc.fill('311')
        self.expiration.fill('05')
        self.expiration_year.fill('2029')

    def click_on_submit(self):
        self.submit.click()

    def succsess(self):
        expect(self.succsess_message).to_be_visible

    def click_on_invoice_download(self):
        with self.page.expect_download(timeout=15000) as download_info:
            self.invoice_download_btn.click()
        return download_info.value

    def click_on_continue_btn(self):
        self.continue_btn.click()

