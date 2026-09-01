from playwright.sync_api import expect
from test_data import TestData
import allure
class Test_auth_TestAutomationExerscis:

    def test_regiester_user(self, home_page, sign_up_page):
       home_page.click_sign_up()
       expect(home_page.new_user_signup_title).to_be_visible()
       sign_up_page.create_test_account_for_test()
       sign_up_page.click_on_delete_account()
       sign_up_page.check_deleted_account()

    @allure.title('Login with correct email and password')
    def test_login_user_with_correct_email_and_password(self, home_page, create_valid_account_for_test, sign_up_page):
        user_data = create_valid_account_for_test
        home_page.click_sign_up()
        expect(home_page.log_in_account_title).to_be_visible() 
        with allure.step('Log in with valid credentials'):
         sign_up_page.login(user_data["email"], user_data["password"])
        expect(home_page.logged_in_user).to_be_visible()
        home_page.click_on_delete_account()
        expect(home_page.deleted_account_title).to_be_visible()

    @allure.title('Login user with incorrect email and password')
    def test_login_user_with_incorrect_email_and_password(self, home_page, sign_up_page):
        home_page.click_sign_up()
        expect(home_page.log_in_account_title).to_be_visible() 
        with allure.step('Log in with invalid credentials'):
         sign_up_page.login(TestData.INVALID_USER["email"], TestData.INVALID_USER["password"])
         expect(sign_up_page.error_message).to_be_visible()

    def test_register_user_with_existing_email(self, home_page, sign_up_page):
        home_page.click_sign_up()
        expect(home_page.new_user_signup_title).to_be_visible()
        sign_up_page.fill_existing_credentials()
        expect(sign_up_page.email_error).to_be_visible()
    