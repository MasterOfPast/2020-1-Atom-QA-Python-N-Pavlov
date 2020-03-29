from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from ui.locators import Auth_Locators


class AuthorizationPage(BasePage):
    locators = Auth_Locators()

    def auth(self, email, password):
        self.click(self.locators.ENTER_BUTTON)
        email_field = self.find(self.locators.EMAIL_LOCATION)
        password_field = self.find(self.locators.PASSWORD_LOCATION)
        email_field.clear()
        password_field.clear()
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
