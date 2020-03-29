import pytest
from base_ui import BaseCase
from some_data.authorization import Authorization_Data as AD
from some_data.authorization import Link_Data as LD


class Test(BaseCase):
    @pytest.mark.UI
    def test_auth_good(self):
        self.auth_page.auth(AD.email, AD.password)
        check = self.auth_page.find(self.auth_page.locators.CHECK_LOCATION)
        assert check is not None

    @pytest.mark.UI
    def test_auth_bad(self):
        self.auth_page.auth("123456", "123456789")
        check = self.auth_page.find(self.auth_page.locators.CHECK_FAIL)
        assert check is not None

    @pytest.mark.UI
    def test_advert_company(self, authorization, download_file, name_company):
        self.main_page = authorization
        self.main_page.create_company(LD.link, name_company, download_file)
        element = self.main_page.find(self.main_page.locators.LINK_COMPANY)
        assert element.get_attribute('title') == name_company

    @pytest.mark.UI
    def test_auditorium(self, authorization, name_company):
        self.main_page = authorization
        self.main_page.create_auditorium(name_company)
        assert self.main_page.find_selectors(self.main_page.locators.CHECK_ELEMENT)[-1].get_attribute('title') == name_company

    @pytest.mark.UI
    def test_delete_auditorium(self, authorization, name_company):
        self.main_page = authorization
        self.main_page.create_auditorium(name_company)
        count = len(self.main_page.find_selectors(self.main_page.locators.CHECK_ELEMENT))
        self.main_page.delete_auditorium()
        assert len(self.main_page.find_selectors(self.main_page.locators.CHECK_ELEMENT)) == count - 1
