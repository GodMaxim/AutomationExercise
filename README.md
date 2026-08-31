# AutomationExercise Test Automation
This project is test automation framework for https://automationexercise.com/test_cases using Playwright and Page Object Model (POM).

# Playwright Test Automation Framework

Automated end-to-end testing framework built with Python, Pytest, and Playwright, utilizing the Page Object Model (POM) design pattern and Allure Reports.

## Project Structure

```text
AutomationExercise/
├── .github/
│   └── workflows/
│       └── playwright.yml       # CI/CD pipeline configuration
├── pages/                       # Page Object classes
│   ├── CartPage.py
│   ├── CheckoutPage.py
│   ├── ContactUsPage.py
│   ├── HomePage.py
│   ├── PaymentPage.py
│   ├── ProductsPage.py
│   └── SignUpPage.py
├── test/                        # Test suites
│   ├── auto_test.py
│   ├── test_auth.py
│   ├── test_cart_page.py
│   ├── test_place_order.py
│   └── test_products.py
├── conftest.py                  # Pytest fixtures and configurations
├── test_data.py                 # Test data sets
└── requirements.txt             # Project dependencies
```

# Features

- Page Object Model (POM): Clean separation of test logic and UI element locators.
- Cross-Browser Testing: Run tests on Chromium, Firefox, or Webkit via CLI options.
- Parallel Execution Matrix: GitHub Actions workflow configured to run test suites across multiple browsers in parallel.
- Allure Reporting: Comprehensive test reporting with step descriptions, attachments, and screenshots.
- CI/CD Integration: Automated deployment of Allure reports to GitHub Pages.
- Slack Notifications: Automated pipeline updates and alert reporting directly to a Slack channel.

# Installation & Setup

 ## Clone the repository: 
 - git clone [https://github.com/GodMaxim/AutomationExercise] (https://github.com/GodMaxim/AutomationExercise)
 - cd AutomationExercise
 
 ## Create and activate a virtual environment: 
 - python -m venv .venv
 - source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

 ## Install dependencies:
 - python -m pip install --upgrade pip
 - pip install -r requirements.txt
 - playwright install --with-deps
 - pip install pytest-rerunfailures

 ## Install Playwright browsers:
 - playwright install

# Running Tests Locally

 ## Run tests using default settings (Chromium browser):
 - pytest
 
 ## Run tests on a specific browser (e.g., Firefox or Webkit) in headless mode with Allure generation:
 - pytest --browser_name=firefox --headless --alluredir=allure-results

 ## To view the generated Allure report locally:
 - allure serve allure-results

# CI/CD Pipeline
The project includes a GitHub Actions workflow (playwright.yml) that triggers on pushes and pull requests to the main/master branches. It executes the following steps:

1. Installs all required dependencies and Playwright browsers across matrix environments.
2. Runs the test suite in parallel for Chromium, Firefox, and Webkit.
3. Merges all test results into a unified Allure report.
3. Publishes the HTML report to GitHub Pages.
4. Sends automated notifications regarding the test run status to Slack. 
```