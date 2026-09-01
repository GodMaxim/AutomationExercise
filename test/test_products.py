from playwright.sync_api import expect
class Test_products_TestAutomationExercise:

    def test_verify_all_products_and_product_detail_page(self, home_page, products_page):
        home_page.click_on_products_btn()
        expect(products_page.title).to_be_visible()
        expect(products_page.products.first).to_be_visible()
        products_page.products_are_visible()
        products_page.click_on_view_product()
        expect(products_page.product_name).to_be_visible()
        expect(products_page.category).to_be_visible()
        expect(products_page.price).to_be_visible()
        expect(products_page.availability).to_be_visible()
        expect(products_page.condition).to_be_visible()
        expect(products_page.brand).to_be_visible()

    def test_search_product(self, home_page, products_page):
        home_page.click_on_products_btn()
        expect(products_page.title).to_be_visible()
        products_page.search_product()
        products_page.check_related_products()

    def test_view_category_products(self, home_page, products_page):
        expect(home_page.category_title).to_be_visible()
        home_page.click_women_category()
        home_page.click_on_dress_category()
        products_page.verify_page_loaded("Women - Dress Products")
        products_page.click_on_men_category_page()

    def test_view_and_cart_brand_products(self, home_page, products_page):
        home_page.click_on_products_btn()
        products_page.see_brends()
        expect(products_page.brends_title).to_be_visible()
        products_page.click_on_polo_btn()
        expect(products_page.polo_title).to_be_visible()
        expect(products_page.page).to_have_url('https://automationexercise.com/brand_products/Polo')
        products_page.click_on_biba_btn()
        expect(products_page.page).to_have_url('https://automationexercise.com/brand_products/Biba')
        expect(products_page.biba_products.first).to_be_visible()
        products_page.verify_biba_page()

    def test_add_review_on_product(self, home_page, products_page):
        home_page.click_on_products_btn()
        expect(products_page.title).to_be_visible()
        products_page.click_on_view_product()
        expect(products_page.reviews_title).to_be_visible()
        products_page.write_a_review()
        products_page.see_thanks_message('Thank you for your review.')
    