import allure
from test_data import TestData
from playwright.sync_api import expect
class TestAutomationExerscis:

    @allure.title('Logout user')
    def test_logout_user(self, home_page, create_valid_account_for_test, sign_up_page):
        user_data = create_valid_account_for_test
        home_page.click_sign_up()
        home_page.check_log_in_title()
        with allure.step('Log in with valid credentials'):
         sign_up_page.log_in_email_input.fill(user_data["email"])
         sign_up_page.log_in_password_input.fill(user_data["password"])
         sign_up_page.click_on_log_in_btn()
        home_page.check_logged_in_as()
        home_page.click_on_logout()

    def test_contact_us_form(self, home_page, contact_us_page):
        home_page.click_on_contact_us()
        contact_us_page.fill_inputs()
        contact_us_page.check_message_and_return()

    def test_verify_test_cases_page(self, home_page, page):
        home_page.click_on_test_cases_btn()
        expect(page).to_have_url('https://automationexercise.com/test_cases')

    def test_verify_subscription_in_home_page(self, home_page):
        home_page.check_subscribe_title()
        home_page.subscribe_action()
        home_page.succsess_message()

    @allure.title('Search products and verify cart after logjn')
    def test_search_products_and_verify_cart_after_login(self, home_page, create_valid_account_for_test, products_page, cart_page, sign_up_page):
        user_data = create_valid_account_for_test
        home_page.click_on_products_btn()
        products_page.check_title()
        products_page.search_product()
        products_page.check_related_products()
        products_page.hover_add_first_product()
        products_page.continue_shopping()
        products_page.hover_add_second_product()
        products_page.click_on_view_cart()
        cart_page.click_on_sign_up_btn()
        with allure.step('Log in with valid credentials'):
         sign_up_page.log_in_email_input.fill(user_data["email"])
         sign_up_page.log_in_password_input.fill(user_data["password"])
         sign_up_page.click_on_log_in_btn()
        home_page.click_on_cart_btn()
        cart_page.see_carts()
        home_page.click_on_delete_account()

    def test_verify_address_details_in_checkout_page(self, home_page, sign_up_page, cart_page, checkout_page):
        home_page.click_sign_up()
        sign_up_page.create_test_account_for_test()
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        checkout_page.check_address()
        checkout_page.click_on_delete_account()
        checkout_page.check_deleted_account()

    @allure.title('Download invoice after purchase order')
    def test_download_invoice_after_purchase_order(self, home_page, cart_page, sign_up_page, checkout_page, payment_page):
        home_page.add_products()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        cart_page.click_on_checkout_login()
        sign_up_page.create_test_account_for_test()
        home_page.click_on_cart_btn()
        cart_page.click_proceed_btn()
        checkout_page.check_address()
        checkout_page.place_order_with_description()
        payment_page.fill_inputs()
        with allure.step('Check that invoice dowloaded after succsessful purchase'):
         payment_page.click_on_submit()
         payment_page.succsess()
         download = payment_page.click_on_invoice_download()
         if download:
            assert download.suggested_filename == "invoice.txt"
        payment_page.click_on_continue_btn()
        home_page.click_on_delete_account()
        home_page.check_deleted_account()

    def test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(self, home_page):
        home_page.check_subscribe_title()
        home_page.scroll_up_by_button()
        expect(home_page.header_text).to_be_visible()

    def test_verify_scroll_up_without_arrow_button_and_scroll_down_functionality(self, home_page):
        home_page.check_subscribe_title()
        home_page.scroll_up_withount_button()

    









      



        
