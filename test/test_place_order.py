from test_data import TestData
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
        checkout_page.check_info()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        payment_page.click_on_submit()
        payment_page.succsess()
        home_page.click_on_delete_account()
        home_page.check_deleted_account()

    @allure.title('Place order register before checkout')
    def test_place_order_register_before_checkout(self, home_page, sign_up_page, payment_page, cart_page, checkout_page):
        home_page.click_sign_up()
        sign_up_page.create_test_account_for_test()
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        with allure.step('Verify Address Details and Review Your Order'):
         checkout_page.check_info()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        payment_page.click_on_submit()
        payment_page.succsess()
        home_page.click_on_delete_account()
        home_page.check_deleted_account()

    @allure.title('Place order login before checkout')
    def test_place_order_login_before_checkout(self, home_page, payment_page, cart_page, checkout_page, sign_up_page, create_valid_account_for_test):
        home_page.click_sign_up()
        sign_up_page.log_in_email_input.fill(TestData.VALID_USER["email"])
        sign_up_page.log_in_password_input.fill(TestData.VALID_USER["password"])
        sign_up_page.click_on_log_in_btn()
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        checkout_page.check_info()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        payment_page.click_on_submit()
        payment_page.succsess()
        home_page.click_on_delete_account()
        home_page.check_deleted_account()
