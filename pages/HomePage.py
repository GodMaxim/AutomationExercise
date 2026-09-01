from playwright.async_api import expect

class HomePage:
    def __init__(self,page):
        self.page = page
        self.sign_up_btn = page.locator('a[href="/login"]')
        self.new_user_signup_title = page.locator('h2', has_text="New User Signup!")
        self.log_in_account_title = page.locator('h2', has_text="Login to your account")
        self.logged_in_user = page.locator('a', has_text="Logged in as")
        self.delete_account_btn = page.locator('a[href="/delete_account"]')
        self.deleted_account_title = page.locator('h2', has_text='Account Deleted')
        self.logout_btn = page.locator('a[href="/logout"]')
        self.contact_us_btn = page.locator('a[href="/contact_us"]')
        self.test_cases_btn = page.locator('#header a[href="/test_cases"]')
        self.products_btn = page.locator('a[href="/products"]')
        self.subscription_title = page.locator('h2', has_text="Subscription")
        self.subscription_input = page.locator('#susbscribe_email')
        self.subscription_btn = page.locator('#subscribe')
        self.succsess_subscribe = page.locator('#success-subscribe')
        self.cart_btn = page.locator('#header a[href="/view_cart"]')
        self.view_product = page.locator('a[href="/product_details/1"]')
        self.first_product = page.locator('.features_items .single-products').first
        self.second_product = page.locator('.features_items .single-products').nth(1)
        self.first_product_add_btn = self.first_product.locator('.product-overlay .add-to-cart')
        self.second_product_add_btn = self.second_product.locator('.product-overlay .add-to-cart')
        self.continue_shopping_btn = page.locator('#cartModal button.btn-success.close-modal')
        self.category_title = page.locator('h2', has_text="Category")
        self.women_category = page.locator('a[href="#Women"]')
        self.dress_category = page.locator('a[href="/category_products/1"]')
        self.recommendation_title = page.locator('h2', has_text="recommended items")
        self.recommended_cart = page.locator('#recommended-item-carousel a.add-to-cart[data-product-id="4"]')
        self.scroll_up_button = page.locator("#scrollUp")
        self.header_text = page.locator('#slider', has_text="Full-Fledged practice website for Automation Engineers")

    def click_sign_up(self):
        self.sign_up_btn.click()

    def click_on_delete_account(self):
        self.delete_account_btn.click()
        self.page.wait_for_url("**/delete_account", timeout=20000)

    def click_on_logout(self):
        self.logout_btn.click()
        expect(self.page).to_have_url('https://automationexercise.com/login')

    def click_on_contact_us(self):
        self.contact_us_btn.click()

    def click_on_test_cases_btn(self):
        self.test_cases_btn.click()

    def click_on_products_btn(self):
        self.products_btn.click()

    def check_subscribe_title(self):
        self.subscription_title.scroll_into_view_if_needed()

    def subscribe_action(self):
        self.subscription_input.fill('coolemail@gmail.com') 
        self.subscription_btn.click()

    def click_on_cart_btn(self):
        self.cart_btn.click(force=True)

    def click_on_view_product(self):
        self.view_product.click()
        expect(self.page).to_have_url('https://automationexercise.com/product_details/1')

    def add_products(self):
        self.first_product.hover()
        self.first_product_add_btn.click()
        self.continue_shopping_btn.click()
        self.second_product.hover()
        self.second_product_add_btn.click()
        self.continue_shopping_btn.click()

    def click_women_category(self):
        self.women_category.click()

    def click_on_dress_category(self):
        self.dress_category.click()

    def see_recommendations(self):
        self.recommendation_title.scroll_into_view_if_needed()

    def click_on_rec_cart(self):
        self.recommended_cart.click()

    def scroll_up_by_button(self):
        self.page.evaluate("window.scrollTo(0, 1000)")
        self.scroll_up_button.click()

    def scroll_up_withount_button(self):
        self.header_text.scroll_into_view_if_needed()
        





    




