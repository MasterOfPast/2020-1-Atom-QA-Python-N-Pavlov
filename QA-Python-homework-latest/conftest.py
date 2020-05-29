import pytest
from fixtures.fixtures_ui import *
from fixtures.fixtures import *
from fixtures.fixtures_api import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://192.168.99.100:1000/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}
