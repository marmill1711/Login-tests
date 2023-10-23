from seleniumpagefactory.Pagefactory import PageFactory


class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    locators = {
        "search": ("ID", "APjFqb"),
        "gmail_button": ("CSS", "#gb > div > div:nth-child(1) > div > div:nth-child(1) > a"),
        "policy_accept": ("CSS", "#L2AGLb > div:nth-child(1)"),
        "policy_denied": ("CSS", "#W0wltc > div:nth-child(1)")
    }

    def click_gmail_button(self):
        self.gmail_button.click()

    def accept_policy(self):
        self.policy_accept.click()

    def denied_policy(self):
        self.denied_policy.click()



