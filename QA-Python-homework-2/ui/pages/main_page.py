from .base_page import BasePage
from ui.locators import Main_Locators
import time


class MainPage(BasePage):

    locators = Main_Locators()

    def create_company(self, link, name, picture):
        try:
            self.click(self.locators.LINK_CREATE_COMPANY)
        except Exception:
            self.click(self.locators.LINK_ZERO_COMPANY)
        self.click(self.locators.TYPE_OF_COMPANY)
        self.completion(link, self.locators.LINK_FIELD)
        self.completion(name, self.locators.NAME_FIELD)
        self.click(self.locators.BANNER)
        download_elem = self.find(self.locators.DOWNLOAD_ELEMENT)
        download_elem.send_keys(picture)
        self.click(self.locators.BUTTON_CREATE_COMPANY)

    def create_auditorium(self, name):
        self.click(self.locators.BUTTON_AUDITORIUM)
        try:
            self.click(self.locators.LINK_ZERO_AUDITORIUM)
        except Exception:
            self.click(self.locators.LINK_CREATE_AUDITORIUM)

        self.completion(name, self.locators.NAME_SEGMENT_FIELD)
        self.click(self.locators.ADD_SEGMENTS)
        self.click(self.locators.OPTION_SEGMENT)
        self.click(self.locators.FIRST_CHECKBOX)
        self.click(self.locators.BUTTON_OPTION)
        self.click(self.locators.SECOND_CHECKBOX)
        self.click(self.locators.BUTTON_CREATE_OPTION)
        self.click(self.locators.CREATE_SEGMENT)
        time.sleep(7)

    def find_selectors(self, locator):
        self.click(self.locators.CLICK_ELEMENT)
        return self.driver.find_elements(*locator)

    def delete_auditorium(self):
        selector = self.find_selectors(self.locators.DELETE_ELEMENT)[-1]
        selector.click()
        self.click(self.locators.DELETE_BUTTON)
