from playwright.sync_api import expect

class CartPage:
    def __init__(self,page):
        self.page = page
        self.subscription_title = page.locator('h2', has_text="Subscription")
        self.subscription_input = page.locator('#susbscribe_email')
        self.subscription_btn = page.locator('#subscribe')
        self.success_subscribe = page.locator('#success-subscribe')
        self.product_1 = page.locator('#product-1')
        self.product_2 = page.locator('#product-2')
        self.proceed = page.locator('a.btn.btn-default.check_out')
        self.checkout_login_btn = page.locator('#checkoutModal a[href="/login"]')
        self.cart_delete = page.locator('a.cart_quantity_delete')
        self.empty_cart_message = page.locator('#empty_cart')
        self.sign_up_btn = page.locator('#header a[href="/login"]')
        self.carts_field = page.locator('#cart_info_table')
        self.visible_carts = page.locator('#checkoutModal')
        
    def check_subscribe_title(self):
        self.subscription_title.scroll_into_view_if_needed()
    
    def subscribe_action(self):
        self.subscription_input.fill('coolemail@gmail.com') 
        self.subscription_btn.click()

    def verify_product_1_details(self, price, quantity, total):
        expect(self.product_1.locator('.cart_price')).to_have_text(price)
        expect(self.product_1.locator('.cart_quantity button')).to_have_text(quantity)
        expect(self.product_1.locator('.cart_total')).to_have_text(total)

    def verify_product_2_details(self, price, quantity, total):
        expect(self.product_2.locator('.cart_price')).to_have_text(price)
        expect(self.product_2.locator('.cart_quantity button')).to_have_text(quantity)
        expect(self.product_2.locator('.cart_total')).to_have_text(total)

    def verify_product_1_quantity(self, quantity):
        expect(self.product_1.locator('.cart_quantity button')).to_have_text(quantity)

    def click_proceed_btn(self):
        expect(self.proceed).to_be_enabled()
        self.proceed.click(delay=150)
        modal = self.page.locator("#checkoutModal")
        try:
            modal.wait_for(state="visible", timeout=1000)
            return
        except:
            pass
        try:
            self.page.wait_for_url("**/checkout", timeout=5000)
        except:
            if "view_cart" in self.page.url:
                self.page.goto("https://automationexercise.com/checkout")
        
    def click_on_checkout_login(self):
        self.checkout_login_btn.wait_for(state="visible", timeout=30000)
        self.checkout_login_btn.click()
        expect(self.page).to_have_url('https://automationexercise.com/login')

    def delete_all_products(self):
        while self.cart_delete.count() > 0:
            first_delete_btn = self.cart_delete.first
            first_delete_btn.evaluate("node => node.click()")
            self.page.wait_for_timeout(500)

    def click_on_sign_up_btn(self):
        self.sign_up_btn.click()


    