from playwright.sync_api import expect
import time

class SignUpPage:
     def __init__(self,page):
          self.page = page
          self.title = page.locator('h2', has_text='Enter Account Information')
          self.gender_btn = page.locator('#id_gender1')
          self.name_input = page.locator('#name')
          self.password_input = page.locator('#password')
          self.day_btn = page.locator('#days')
          self.months_btn = page.locator('#months')
          self.years_btn = page.locator('#years')
          self.newsletter_btn = page.locator('#newsletter')
          self.spec_offers_btn = page.locator('#optin')
          self.first_name_input = page.locator('#first_name')
          self.last_name_input = page.locator('#last_name')
          self.company_input = page.locator('#company')
          self.address1_input = page.locator('#address1')
          self.address2_input = page.locator('#address2')
          self.country_select = page.locator('#country')
          self.state_input = page.locator('#state')
          self.city_input = page.locator('#city')
          self.zipcode_input = page.locator('#zipcode')
          self.mobile_number = page.locator('#mobile_number')
          self.create_account_submit = page.locator('button[data-qa="create-account"]')
          self.created_title = page.locator('h2', has_text='Account Created!')
          self.continue_btn = page.locator('a[data-qa="continue-button"]')
          self.logged_in_user = page.locator('a', has_text="Logged in as")
          self.delete_account_btn = page.locator('a[href="/delete_account"]')
          self.deleted_account_title = page.locator('h2', has_text='Account Deleted')
          self.name_input_login = page.locator('input[data-qa="signup-name"]')
          self.email_input = page.locator('input[data-qa="signup-email"]')
          self.submit_btn = page.locator('button[data-qa="signup-button"]')
          self.log_in_btn = page.locator('button[data-qa="login-button"]')
          self.error_message = page.locator('p', has_text="Your email or password is incorrect!")
          self.log_in_email_input = page.locator('input[data-qa="login-email"]')
          self.log_in_password_input = page.locator('input[data-qa="login-password"]')
          self.email_error = page.locator('p', has_text="Email Address already exist!")
          unique_email = f"user_{int(time.time() * 1000)}@gmail.com"

     def check_title(self):
          expect(self.title).to_be_visible()

     def check_error_message(self):
          expect(self.error_message).to_be_visible()

     def click_on_log_in_btn(self):
          self.log_in_btn.click()  

     def fill_inputs_login(self):
          self.name_input_login.wait_for(state="visible", timeout=10000)
          self.name_input_login.fill('Somename')
          unique_email = f"user_{int(time.time())}@gmail.com"
          self.email_input.fill(unique_email)
          self.submit_btn.click()
          self.title.wait_for(state="visible", timeout=15000)
     
     def fill_valid_user(self):
          self.name_input_login.fill('My')
          self.email_input.fill('correctone@gmail.com')
          self.submit_btn.click()  

     def fill_inputs(self):
          self.page.wait_for_url("**/signup", timeout=20000)
          self.page.wait_for_load_state("domcontentloaded")
          self.gender_btn.wait_for(state="visible", timeout=30000)
          self.gender_btn.click(force=True)
          self.name_input.fill('Somename')
          self.password_input.fill('Greatpassword123')

     def fill_exesting_credentials(self):
          self.name_input_login.fill('Somename')
          self.email_input.fill('myemail@gmail.com')
          self.submit_btn.click()

     def date_of_birth(self, day, months, year):
          self.day_btn.select_option(day)
          self.months_btn.select_option(months)
          self.years_btn.select_option(year)

     def click_on_checkboxes(self):
          self.newsletter_btn.click() 
          self.spec_offers_btn.click() 

     def address_information(self, country): 
          self.first_name_input.fill('Somename')   
          self.last_name_input.fill('SomeLastName')
          self.company_input.fill('GoodCompany')
          self.address1_input.fill('Baker St.')
          self.address2_input.fill('Not Baker St.')
          self.country_select.select_option(country)
          self.state_input.fill('UnitedOne')
          self.city_input.fill('The best one')
          self.zipcode_input.fill('12345')
          self.mobile_number.fill('1234')

     def fill_valid_input(self):
          self.gender_btn.wait_for(state="visible", timeout=25000)
          self.gender_btn.click(force=True)
          self.name_input.fill('My')
          self.password_input.fill('CorrectPassword')

     def address_valid_information(self, country):
          self.first_name_input.fill('My')   
          self.last_name_input.fill('Last')
          self.company_input.fill('Mine')
          self.address1_input.fill('None')
          self.address2_input.fill('None 2')
          self.country_select.select_option(country)
          self.state_input.fill('United')
          self.city_input.fill('The good')
          self.zipcode_input.fill('12345')
          self.mobile_number.fill('12345')

     def click_on_submit_create_account(self):
          self.create_account_submit.click()
               
     def check_created_title(self):
          expect(self.created_title).to_be_visible()

     def click_contiue_btn(self):
          self.continue_btn.click()

     def check_logged_in_as(self):
          expect(self.logged_in_user).to_be_visible()     

     def click_on_delete_account(self):
          self.delete_account_btn.wait_for(state="visible", timeout=30000)
          self.delete_account_btn.click()

     def check_deleted_account(self):
          expect(self.deleted_account_title).to_be_visible()   
          self.continue_btn.click()    

     def see_email_error(self):
          expect(self.email_error).to_be_visible()

     def create_test_account_for_test(self):
          self.fill_inputs_login()
          self.fill_inputs()
          self.date_of_birth("5", "May", "1995")
          self.click_on_checkboxes()
          self.address_information("United States")
          self.click_on_submit_create_account()
          self.check_created_title()  
          self.click_contiue_btn()
          self.check_logged_in_as()




              

               
          

