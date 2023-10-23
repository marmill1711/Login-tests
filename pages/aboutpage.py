from seleniumpagefactory.Pagefactory import PageFactory


class AboutPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    locators = {
        'sign_in_button': ('xpath', '/html/body/header/div/div/div/a[2]')
    }

    def get_title(self):
        return self.driver.title

    def click_sign_in_button(self):
        self.sign_in_button.click()
