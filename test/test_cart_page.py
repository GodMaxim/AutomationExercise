import allure
from playwright.async_api import expect
class Test_cart_page_TestAutomationExercise:

    def test_verify_subscription_in_cart_page(self, home_page, cart_page):
        home_page.click_on_cart_btn()
        cart_page.check_subscribe_title()
        expect(cart_page.subscription_title).to_be_visible()
        cart_page.subscribe_action()
        expect(cart_page.success_subscribe).to_be_visible()

    @allure.title('Add products in cart')
    def test_add_products_in_cart(self, home_page, cart_page, products_page):
        home_page.click_on_products_btn()
        products_page.hover_add_first_product()
        products_page.continue_shopping()
        products_page.hover_add_second_product()
        products_page.click_on_view_cart()
        with allure.step('Veirfy that products added to cart and their prices, quantity and total price are visible'):
         expect(cart_page.product_1).to_be_visible()
         expect(cart_page.product_2).to_be_visible()
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
        expect(cart_page.empty_cart_message).to_be_visible()

    def test_add_to_cart_from_recommended_items(self, home_page, cart_page):
        home_page.see_recommendations()
        expect(home_page.recommendation_title).to_be_visible()
        home_page.click_on_rec_cart()
        home_page.click_on_cart_btn()
        expect(cart_page.carts_field).to_be_visible()