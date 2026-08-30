from playwright.sync_api import expect

class ContactUsPage:
    def __init__(self,page):
        self.page = page
        self.title = page.locator('h2', has_text="Get In Touch")
        self.name_input = page.locator('input[data-qa="name"]')
        self.email_input = page.locator('input[data-qa="email"]')
        self.subject_input = page.locator('input[data-qa="subject"]')
        self.message_field = page.locator('#message')
        self.upload_file = page.locator('input[type="file"]')
        self.submit_btn = page.locator('input[data-qa="submit-button"]')
        self.succsess_message = page.locator('.status.alert.alert-success')
        self.back_home_btn = page.locator('.btn.btn-success')

    def fill_inputs(self):
        self.page.wait_for_load_state("networkidle")
        self.name_input.fill('Name')
        self.email_input.fill('coolemail@gmail.com')
        self.subject_input.fill('About testing')
        self.message_field.fill('Good site, bro')
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_btn.scroll_into_view_if_needed()
        self.submit_btn.dispatch_event("click")
        self.page.wait_for_timeout(3000)

    def check_message_and_return(self):
        expect(self.succsess_message).to_be_visible(timeout=10000)
        self.back_home_btn.click()
        expect(self.page).to_have_url('https://automationexercise.com/')
