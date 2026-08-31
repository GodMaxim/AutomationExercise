class TestData:
    TEST_USER = {
        "name": "Somename",
        "email": "coolemail@gmail.com",
        "password": "Greatpassword123"
    }

    INVALID_USER = {
        "name": "1",
        "email": "1@gmail.com",
        "password": "2"
        }

    BROWSER_ACCOUNTS = {
        "chromium": {"email": "user_chromium@test.com", "password": "password123"},
        "firefox": {"email": "user_firefox@test.com", "password": "password123"}
    }