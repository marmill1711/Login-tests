from selenium import webdriver
from pages.sign_in_page import SignInPage


def test_proper_login():
    """
    This TC cheks proper login with valid email/phone and password.
    """
    driver = webdriver.Chrome()
    sign_in_page = SignInPage(driver)

    # Step1 - Go to https://accounts.google.com/
    driver.get("https://accounts.google.com/")
    assert sign_in_page.get_email_box_text() == "Email or phone"

    sign_in_page.check_heading_text()
