from selenium import webdriver

from pages.aboutpage import AboutPage
from pages.homepage import Homepage
from pages.sign_in_page import SignInPage


def test_navigate_to_login_page():
    """
    This TC checks is it possible to navigate to gmail login page.
    """
    driver = webdriver.Chrome()
    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)
    about_page = AboutPage(driver)

    # Step1 - Go to the www.google.com
    driver.get("https://www.google.com")

    # Step2 - Accept the policy
    homepage.accept_policy()

    # Step3 - Click 'Gmail" button
    homepage.click_gmail_button()

    # Step4 - On the Gmail About website click Sign In button
    assert about_page.get_title() == 'Gmail: Private and secure email at no cost | Google Workspace'
    about_page.click_sign_in_button()
    assert sign_in_page.check_heading_text() == 'Sign in'






