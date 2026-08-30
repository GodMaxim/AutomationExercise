import pytest
import allure
from playwright.sync_api import sync_playwright, expect
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
from pages.ContactUsPage import ContactUsPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.PaymentPage import PaymentPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", 
        action="store", 
        default="chromium", 
        help="Browser to run tests: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--headless", 
        action="store_true", 
        default=False, 
        help="Run tests in headless mode"
    )

@pytest.fixture(scope="function")
def page(request):
    browser_type_name = request.config.getoption("--browser_name")
    is_headless = request.config.getoption("--headless")
    
    browser_args = []
    if browser_type_name == "chromium":
        browser_args = [
            "--disable-translate",
            "--disable-features=Translate,TranslateUI",
            "--lang=en-US"
        ]

    with sync_playwright() as p:
        browser_type = getattr(p, browser_type_name)
        browser = browser_type.launch(
            headless=is_headless,
            args=browser_args
        )
        context = browser.new_context(
            locale="en-US",
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
            viewport={"width": 1366, "height": 768}
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.set_default_timeout(10000)
        expect.set_options(timeout=10000)
        page.route("**/adsbygoogle.js", lambda route: route.abort())
        page.route("**/pagead2.googlesyndication.com/**", lambda route: route.abort())
        page.route("**/google_vignette**", lambda route: route.abort())
        page.route("**/translate.googleapis.com/**", lambda route: route.abort())
        page.route("**/translate.google.com/**", lambda route: route.abort())
        page.route("**/*translate_a*", lambda route: route.abort())
        page.goto("https://automationexercise.com/", wait_until="domcontentloaded", timeout=30000)
        page.evaluate("""
        () => {
            const ads = document.querySelectorAll('iframe, ins, .adsbygoogle, [id*="google_ads"]');
            ads.forEach(ad => ad.remove());
        }
    """)

        yield page
        context.tracing.stop(path="trace.zip")
        allure.attach.file("trace.zip", name="trace", attachment_type=allure.attachment_type.ZIP if hasattr(allure.attachment_type, "ZIP") else allure.attachment_type.TEXT)
        page.close()
        context.close()
        browser.close()

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def sign_up_page(page):
    return SignUpPage(page)

@pytest.fixture
def contact_us_page(page):
    return ContactUsPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)

@pytest.fixture
def payment_page(page):
    return PaymentPage(page)

@pytest.fixture
def create_valid_account_for_test(page, home_page, sign_up_page):
    home_page.click_sign_up()
    sign_up_page.fill_valid_user()
    sign_up_page.fill_valid_input()
    sign_up_page.address_valid_information("United States")
    sign_up_page.click_on_submit_create_account()
    sign_up_page.click_contiue_btn()
    home_page.click_on_logout()
    page.goto("https://automationexercise.com/")


