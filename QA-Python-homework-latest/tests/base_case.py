import pytest
from ui.pages.start_page import StartPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.page: StartPage = request.getfixturevalue('start_page')


class BaseCaseCreate:
    @pytest.fixture(scope='function', autouse=True)
    def setup_create(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.page: StartPage = request.getfixturevalue('open_create')


class BaseCaseMain:
    @pytest.fixture(scope='function', autouse=True)
    def setup_main(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.page: StartPage = request.getfixturevalue('open_main')
