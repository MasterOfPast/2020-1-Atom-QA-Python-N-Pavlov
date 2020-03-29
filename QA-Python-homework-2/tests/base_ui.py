import pytest
from ui.pages.authorization_page import AuthorizationPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.auth_page: AuthorizationPage = request.getfixturevalue('auth_page')
