import time

from selenium import webdriver

from pages.sign_in_page import SignInPage

INVALID_ADDRESS_LIST= [
    "A@b@c@gmail.com",
    "a'b(c)d,e:f;gi[j\k]l@example.com",
    "this is'notallowed@gmail.com",
    "this\ still'not'allowed@gmail.com",
    "1234567890123456789012345678901234567890123456789012345678901234+x@gmail.com",
    "example@localhost",
    "john.doe@gmail..com",
    "'much.more unusual'@gmail.com",
]


def test_invalid_address():
    """
    This TC checks if it is possible to login with invalid address email.
    """
    driver = webdriver.Chrome()
    sign_in_page = SignInPage(driver)

    # Step1 - Go to https://accounts.google.com/
    driver.get("https://accounts.google.com/")

    for invalid_address in INVALID_ADDRESS_LIST:
        # Step2 - Use an invalid address
        sign_in_page.send_keys_to_email_box(invalid_address)
        time.sleep(2)
        sign_in_page.click_next_button()
        sign_in_page.clear_email_box()
        # Step3 - Check if "Enter a valid email or phone number" is displayed
        assert sign_in_page.check_invalid_error() == "Enter a valid email or phone number"


