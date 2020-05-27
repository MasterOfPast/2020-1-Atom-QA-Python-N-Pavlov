from .Base_page import BasePage
from ui.locators import Create_locators


class CreatePage(BasePage):
    locators = Create_locators()

    def create_user(self, user, email, password, confirm=True):
        self.completion(user, self.locators.USER_FIELD)
        self.completion(email, self.locators.EMAIL_FILED)
        self.completion(password, self.locators.PASSWORD_FIELD)
        if confirm:
            self.completion(password, self.locators.CONFIRM_FIELD)
        else:
            self.completion(password + 'not', self.locators.CONFIRM_FIELD)
        self.click(self.locators.TERM)
        self.click(self.locators.CREATE_BUTTON)

    def to_auth(self):
        self.click(self.locators.AUTH_LINK)
