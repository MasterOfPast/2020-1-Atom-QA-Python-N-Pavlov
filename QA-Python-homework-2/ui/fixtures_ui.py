import pytest
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.authorization_page import AuthorizationPage
from selenium import webdriver
from some_data.authorization import Authorization_Data as AD
import os
import random
from selenium.webdriver import ChromeOptions


class UndifinedBrowser(Exception):
    pass


@pytest.fixture(scope="function")
def driver(config):
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid']
    url = config['url']
    if browser == "chrome":
        if not selenoid:
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install())
        else:
            capabilities = {
                'browserName': browser,
                'version': '80.0'
            }
            options = ChromeOptions()
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities=capabilities)
    else:
        raise UndifinedBrowser(f'Ввели фигню, нужен chrome, {browser} ересь')
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope="function")
def auth_page(driver):
    return AuthorizationPage(driver)


@pytest.fixture(scope="function")
def authorization(driver):
    page = AuthorizationPage(driver)
    page.auth(AD.email, AD.password)
    return MainPage(page.driver)


@pytest.fixture(scope="function")
def download_file():
    fixtures_path = os.path.dirname(__file__)
    path = os.path.join(fixtures_path, "..", "some_data", "Concept_Car.jpg")
    path = os.path.abspath(path)
    return path


@pytest.fixture(scope='function')
def name_company():
    return "test_name" + str(random.randint(1, 1000))
