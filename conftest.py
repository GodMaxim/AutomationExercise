import pytest
import allure
import os
from test_data import TestData
from playwright.sync_api import sync_playwright, expect
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
from pages.ContactUsPage import ContactUsPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.PaymentPage import PaymentPage

@pytest.fixture(scope="function", autouse=True)
def configure_playwright_environment(page, context, request):
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """)
    
    page.set_default_timeout(20000)
    expect.set_options(timeout=20000)
    
    page.route("**/adsbygoogle.js", lambda route: route.abort())
    page.route("**/pagead2.googlesyndication.com/**", lambda route: route.abort())
    page.route("**/google_vignette**", lambda route: route.abort())
    page.route("**/translate.googleapis.com/**", lambda route: route.abort())
    page.route("**/translate.google.com/**", lambda route: route.abort())
    page.route("**/*translate_a*", lambda route: route.abort())

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded", timeout=30000)
    
    page.evaluate("""
        () => {
            const ads = document.querySelectorAll('iframe, ins, .adsbygoogle, [id*="google_ads"]');
            ads.forEach(ad => ad.remove());
        }
    """)
    
    yield page
    
    os.makedirs("traces", exist_ok=True)
    trace_path = f"traces/{request.node.name}_trace.zip"
    context.tracing.stop(path=trace_path)
    
    if os.path.exists(trace_path):
        allure.attach.file(
            trace_path, 
            name=f"trace_{request.node.name}", 
            attachment_type="application/zip"
        )

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
def get_browser_user(request):
    browser_name = request.config.getoption("--browser", default="chromium")
    if isinstance(browser_name, list):
        browser_name = browser_name[0]
    return TestData.BROWSER_ACCOUNTS.get(browser_name, TestData.BROWSER_ACCOUNTS["chromium"])

@pytest.fixture
def create_valid_account_for_test(page, home_page, sign_up_page, request):
    browser_name = request.config.getoption("--browser", default="chromium")
    if isinstance(browser_name, list):
        browser_name = browser_name[0]
    current_user = TestData.BROWSER_ACCOUNTS.get(browser_name, TestData.BROWSER_ACCOUNTS["chromium"])
    home_page.click_sign_up()
    sign_up_page.fill_valid_user(name="My", email=current_user["email"])
    sign_up_page.fill_valid_input(password=current_user["password"])
    sign_up_page.address_valid_information("United States")
    sign_up_page.click_on_submit_create_account()
    sign_up_page.click_continue_btn()
    home_page.click_on_logout()
    page.goto("https://automationexercise.com/")
    yield current_user
