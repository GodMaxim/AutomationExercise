from test_data import TestData
import allure

class Test_auth_TestAutomationExerscis:

    def test_regiester_user(self, home_page, sign_up_page):
       home_page.click_sign_up()
       home_page.check_new_user_title()
       sign_up_page.create_test_account_for_test()
       sign_up_page.click_on_delete_account()
       sign_up_page.check_deleted_account()

    @allure.title('Login with correct email and password')
    def test_login_user_with_correct_email_and_password(self, home_page, create_valid_account_for_test, sign_up_page):
        home_page.click_sign_up()
        home_page.check_log_in_title()
        with allure.step('Log in with valid credentials'):
         sign_up_page.log_in_email_input.fill(TestData.VALID_USER["email"])
         sign_up_page.log_in_password_input.fill(TestData.VALID_USER["password"])
         sign_up_page.click_on_log_in_btn()
        home_page.check_logged_in_as()
        home_page.click_on_delete_account()
        home_page.check_deleted_account()

    @allure.title('Login user with incorrect email and password')
    def test_login_user_with_incorrect_email_and_password(self, home_page, sign_up_page):
        home_page.click_sign_up()
        home_page.check_log_in_title()
        with allure.step('Log in with invalid credentials'):
         sign_up_page.log_in_email_input.fill(TestData.INVALID_USER["email"])
         sign_up_page.log_in_password_input.fill(TestData.INVALID_USER["password"])
         sign_up_page.click_on_log_in_btn()
         sign_up_page.check_error_message()

    def test_register_user_with_existing_email(self, home_page, sign_up_page):
        home_page.click_sign_up()
        home_page.check_new_user_title()
        sign_up_page.fill_exesting_credentials()
        sign_up_page.see_email_error()
    