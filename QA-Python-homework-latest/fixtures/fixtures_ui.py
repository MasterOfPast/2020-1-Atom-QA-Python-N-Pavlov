import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from ui.pages.start_page import StartPage
from ui.pages.create_page import CreatePage
from ui.pages.main_page import MainPage
import requests


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


@pytest.fixture()
def start_page(driver):
    return StartPage(driver)


@pytest.fixture(scope="function")
def open_create(driver):
    page = StartPage(driver)
    page.to_create()
    return CreatePage(page.driver)


@pytest.fixture(scope='function')
def open_main(driver, auth_data):
    page = StartPage(driver)
    page.auth(auth_data['user'], auth_data['password'])
    return MainPage(page.driver)


@pytest.fixture()
def get_id():
    requests.get("http://192.168.99.100:5000/add_id/Helloworld")
    return requests.get('http://192.168.99.100:5000/vk_id/Helloworld').json()


@pytest.fixture()
def delete_id():
    requests.get("http://192.168.99.100:5000/delete_id/enter_user")
