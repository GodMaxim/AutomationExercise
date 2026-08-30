class Test_products_TestAutomationExerscis:

    def test_verify_all_products_and_product_detail_page(self, home_page, products_page):
        home_page.click_on_products_btn()
        products_page.check_title()
        products_page.products_are_visible()
        products_page.click_on_view_product()
        products_page.all_details_are_visible()

    def test_search_product(self, home_page, products_page):
        home_page.click_on_products_btn()
        products_page.check_title()
        products_page.search_product()
        products_page.check_related_products()

    def test_view_category_products(self, home_page, products_page):
        home_page.visible_category()
        home_page.click_women_category()
        home_page.click_on_dress_category()
        products_page.verify_page_loaded("Women - Dress Products")
        products_page.click_on_men_category_page()

    def test_view_and_cart_brand_products(self, home_page, products_page):
        home_page.click_on_products_btn()
        products_page.see_brends()
        products_page.click_on_polo_btn()
        products_page.verify_polo_page()
        products_page.click_on_biba_btn()
        products_page.veryfy_biba_page()

    def test_add_review_on_product(self, home_page, products_page):
        home_page.click_on_products_btn()
        products_page.check_title()
        products_page.click_on_view_product()
        products_page.see_review_title()
        products_page.write_a_review()
        products_page.see_thanks_message('Thank you for your review.')
    