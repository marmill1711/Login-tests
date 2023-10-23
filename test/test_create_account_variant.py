from selenium import webdriver


from pages.sign_in_page import SignInPage


def test_create_account_variant():
    """
    This checks proper variants for create account.
    """
    driver = webdriver.Chrome()
    sign_in_page = SignInPage(driver)

    # Step1 - Go to https://accounts.google.com/
    driver.get("https://accounts.google.com/")

    # Step 2 - Click "Create account" button
    sign_in_page.click_create_account()

    # Step 3 - Check if "For my personal use", "For my child", "For work or my business" variants are listed.
    variants = sign_in_page.check_variants().splitlines()
    variants_to_check = [
        "For my personal use",
        "For my child",
        "For work or my business"
    ]
    for variant_to_check in variants_to_check:
        assert variant_to_check in variants

