from playwright.async_api import expect
import allure

class Test_place_order_TestAutomationExerscis:

    @allure.title('Add products in cart')
    def test_place_order_register_while_checkout(self, home_page, cart_page, sign_up_page, checkout_page, payment_page):
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        with allure.step('Register/Login button appears'):
         cart_page.click_on_checkout_login()
        sign_up_page.create_test_account_for_test()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        expect(checkout_page.info).to_be_visible()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        payment_page.click_on_submit()
        expect(payment_page.success_message).to_be_visible()
        home_page.click_on_delete_account()
        expect(home_page.deleted_account_title).to_be_visible()

    @allure.title('Place order register before checkout')
    def test_place_order_register_before_checkout(self, home_page, sign_up_page, payment_page, cart_page, checkout_page):
        home_page.click_sign_up()
        sign_up_page.create_test_account_for_test()
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        with allure.step('Verify Address Details and Review Your Order'):
         expect(checkout_page.info).to_be_visible()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        payment_page.click_on_submit()
        expect(payment_page.success_message).to_be_visible()
        home_page.click_on_delete_account()
        expect(home_page.deleted_account_title).to_be_visible()

    @allure.title('Place order login before checkout')
    def test_place_order_login_before_checkout(self, home_page, payment_page, cart_page, checkout_page, sign_up_page, create_valid_account_for_test):
        user_data = create_valid_account_for_test
        home_page.click_sign_up()
        sign_up_page.login(user_data["email"], user_data["password"])
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        expect(checkout_page.info).to_be_visible()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        payment_page.click_on_submit()
        expect(payment_page.success_message).to_be_visible()
        home_page.click_on_delete_account()
        expect(home_page.deleted_account_title).to_be_visible()
