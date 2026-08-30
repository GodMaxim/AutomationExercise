import allure
class Test_cart_page_TestAutomationExerscis:

    def test_verify_subscription_in_cart_page(self, home_page, cart_page):
        home_page.click_on_cart_btn()
        cart_page.check_subscribe_title()
        cart_page.subscribe_action()
        cart_page.succsess_message()

    @allure.title('Add products in cart')
    def test_add_products_in_cart(self, home_page, cart_page, products_page):
        home_page.click_on_products_btn()
        products_page.hover_add_first_product()
        products_page.continue_shopping()
        products_page.hover_add_second_product()
        products_page.click_on_view_cart()
        with allure.step('Veirfy that products added to cart and their prices, quantity and total price are visible'):
         cart_page.verify_products_in_cart()
         cart_page.verify_product_1_details("Rs. 500", "1", "Rs. 500")
         cart_page.verify_product_2_details("Rs. 400", "1", "Rs. 400")

    def test_verify_product_quantity_in_cart(self, home_page, cart_page, products_page):
        home_page.click_on_view_product()
        products_page.increase_quantity()
        products_page.click_on_view_cart()
        cart_page.verify_product_1_quantity("4")

    def test_remove_products_from_cart(self, home_page, cart_page):
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.delete_all_products()
        cart_page.verify_cart_is_empty()

    def test_add_to_cart_from_recommended_items(self, home_page, cart_page):
        home_page.see_recommendations()
        home_page.click_on_rec_cart()
        home_page.click_on_cart_btn()
        cart_page.see_carts()