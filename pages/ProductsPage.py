from playwright.sync_api import expect

class ProductsPage:
    def __init__(self,page):
        self.page = page
        self.title = page.locator('h2', has_text="All Products")
        self.search_input = page.locator('#search_product')
        self.search_btn = page.locator('#submit_search')
        self.searched_title = page.locator('h2', has_text="Searched Products")
        self.searched_products = page.locator('.features_items .product-image-wrapper')
        self.first_product = page.locator('.features_items .single-products').first
        self.second_product = page.locator('.features_items .single-products').nth(1)
        self.first_product_add_btn = self.first_product.locator('.product-overlay .add-to-cart')
        self.second_product_add_btn = self.second_product.locator('.product-overlay .add-to-cart')
        self.continue_shopping_btn = page.locator('#cartModal button.btn-success.close-modal')
        self.cart_btn = page.locator('#cartModal a[href="/view_cart"]')
        self.quantity_input = page.locator('#quantity')
        self.add_to_cart_btn = page.locator('button.btn.btn-default.cart')
        self.category_title = page.locator('h2.title.text-center')
        self.men_category = page.locator('a[href="#Men"]')
        self.tshirts_men_page = page.locator('a[href="/category_products/3"]')
        self.brends_title = page.locator('h2', has_text="Brands")
        self.polo_btn = page.locator('a[href="/brand_products/Polo"]')
        self.polo_title = page.locator('h2', has_text="Brand - Polo Products")
        self.biba_btn = page.locator('a[href="/brand_products/Biba"]')
        self.biba_products = page.locator(".features_items .col-sm-4")
        self.view_product = page.locator('a[href="/product_details/1"]')
        self.reviews_title = page.locator('a[href="#reviews"]')
        self.name_input = page.locator('#name')
        self.email_input = page.locator('#email')
        self.review_field = page.locator('#review')
        self.submit_review = page.locator('#button-review')
        self.thanks_message = page.locator('#review-section')
        self.product_name = page.locator(".product-information h2")
        self.category = page.locator(".product-information p", has_text="Category")
        self.price = page.locator(".product-information span span")
        self.availability = page.get_by_text("Availability:")
        self.condition = page.get_by_text("Condition:")
        self.brand = page.get_by_text("Brand:")
        self.products = page.locator(".features_items .col-sm-4")

    def check_title(self):
        expect(self.title).to_be_visible()

    def search_product(self):
        self.search_input.fill('Top')
        self.search_btn.click()

    def check_related_products(self):
        expect(self.searched_title).to_be_visible(timeout=20000)
        expect(self.searched_products.first).to_be_visible()
        count = self.searched_products.count()
        assert count > 0, "Products were not found"
        for i in range(count):
            expect(self.searched_products.nth(i)).to_be_visible()

    def hover_add_first_product(self):
        self.first_product.hover()
        self.first_product_add_btn.click()

    def hover_add_second_product(self):
        self.second_product.hover()
        self.second_product_add_btn.click()

    def continue_shopping(self):
        self.continue_shopping_btn.click()

    def click_on_view_cart(self):
        self.cart_btn.click()

    def increase_quantity(self):
        self.quantity_input.fill('4')
        self.add_to_cart_btn.click()

    def verify_page_loaded(self, expected_title: str):
        expect(self.page).to_have_url('https://automationexercise.com/category_products/1')
        expect(self.category_title).to_have_text(expected_title)

    def click_on_men_category_page(self):
        self.men_category.click()
        self.tshirts_men_page.click()
        expect(self.page).to_have_url('https://automationexercise.com/category_products/3')

    def see_brends(self):
        self.brends_title.scroll_into_view_if_needed()
        expect(self.brends_title).to_be_visible()

    def click_on_polo_btn(self):
        self.polo_btn.click()

    def verify_polo_page(self):
        expect(self.polo_title).to_be_visible()
        expect(self.page).to_have_url('https://automationexercise.com/brand_products/Polo')

    def click_on_biba_btn(self):
        self.biba_btn.click()

    def veryfy_biba_page(self):
        expect(self.page).to_have_url('https://automationexercise.com/brand_products/Biba')
        expect(self.biba_products.first).to_be_visible()
        assert self.biba_products.count() > 0

    def click_on_view_product(self):
        self.view_product.click()
        expect(self.page).to_have_url('https://automationexercise.com/product_details/1')

    def see_review_title(self):
        expect(self.reviews_title).to_be_visible()

    def write_a_review(self):
        self.name_input.fill('Me')
        self.email_input.fill('coolemail@gmail.com')
        self.review_field.fill('Not good review')
        self.submit_review.click()

    def see_thanks_message(self, expected_message):
        expect(self.thanks_message).to_have_text(expected_message)

    def all_details_are_visible(self):
        expect(self.product_name).to_be_visible()
        expect(self.category).to_be_visible()
        expect(self.price).to_be_visible()
        expect(self.availability).to_be_visible()
        expect(self.condition).to_be_visible()
        expect(self.brand).to_be_visible()

    def products_are_visible(self):
        expect(self.products.first).to_be_visible()
        assert self.products.count() > 0




