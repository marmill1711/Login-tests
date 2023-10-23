from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory


class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()
        self.wait = WebDriverWait(driver, 10)

    locators = {
        "email_box": ("id", "identifierId"),
        "email_box_text": ("CSS", ".QBQrY > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"),
        "heading_text": ("id", "headingText"),
        "create_account_button": ("CSS", ".VfPpkd-xl07Ob-XxIAqe-OWXEXe-oYxtQd > div:nth-child(1) > div:nth-child(1)"),
        "account_variants": ("CSS", ".VfPpkd-StrnGf-rymPhb"),
        "variant": ("class_name", "G3hhxb VfPpkd-StrnGf-rymPhb-ibnC6b"),
        "next_button": ("CSS", ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)"),
        "password_box": ("CSS", "#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"),
        "try_again_button": ("CSS", "#next > div > div > a"),
        "invalid_error": ("CSS", ".o6cuMc"),
        "languages_button": ("CSS", ".VfPpkd-O1htCb"),
        "languages_list": ("xpath", "/html/body/div[1]/div[1]/footer/div/div/div/div[2]")
    }

    def get_languages_list(self):
        return self.languages_list

    def get_language(self):
        language_list = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/footer/div/div/div/div[2]")
        language = language_list.find_elements(By.CSS_SELECTOR, "li.MCs1Pd:nth-child(2)")
        for i in language:
            text = i.text
            print(text)

    def click_languages_button(self):
        self.languages_button.click()

    def clear_email_box(self):
        self.email_box.clear()

    def check_heading_text(self):
        return self.heading_text.text

    def click_create_account(self):
        self.create_account_button.click()

    def check_variants(self):
        return self.account_variants.text

    def get_email_box_text(self):
        return self.email_box_text.text

    def send_keys_to_email_box(self, input):
        self.email_box.send_keys(input)

    def check_email_box_is_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))

    def click_next_button(self):
        self.next_button.click()

    def get_password_box_value(self):
        return self.password_box.get_attribute('value')

    def click_try_again_button(self):
        self.try_again_button.click()

    def check_invalid_error(self):
        return self.invalid_error.text



