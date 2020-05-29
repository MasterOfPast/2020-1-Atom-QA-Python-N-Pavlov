from .Base_page import BasePage
from ui.locators import Auth_locators


class StartPage(BasePage):
    locators = Auth_locators()

    def auth(self, user, password):
        self.completion(user, self.locators.USER_FIELD)
        self.completion(password, self.locators.PASSWORD_FIELD)
        self.click(self.locators.LOGIN_BUTTON)

    def to_create(self):
        self.click(self.locators.CREATE_LINK)
