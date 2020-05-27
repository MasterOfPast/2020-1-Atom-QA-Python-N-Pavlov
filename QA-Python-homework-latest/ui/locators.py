from selenium.webdriver.common.by import By


class Auth_locators:
    USER_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    TEXT = (By.XPATH, '//h3[contains(text(), "Welcome to the TEST SERVER")]')
    ACCESS_AUTH = (By.XPATH, '//li[contains(text(), "Logged as")]')
    BAN_AUTH = (By.XPATH, '//div[contains(text(), "Ваша учетная запись заблокирована")]')
    FLASH = (By.ID, 'flash')
    USER_LENTH_ERROR = (By.XPATH, '//div[contains(text(), "Incorrect username length")]')
    CREATE_LINK = (By.LINK_TEXT, 'Create an account')
    CREATE_TEXT = (By.XPATH, "//*[@class='uk-card-title uk-text-center']")
    HOME_BUTTON = (By.LINK_TEXT, 'HOME')
    VK_ID = (By.XPATH, '//li[contains(text(), "VK ID:")]')


class Create_locators:
    USER_FIELD = (By.ID, "username")
    EMAIL_FILED = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_FIELD = (By.ID, "confirm")
    AUTH_LINK = (By.LINK_TEXT, 'Log in')
    TEXT = (By.XPATH, '//h3[contains(text(), "Welcome to the TEST SERVER")]')
    ACCESS_CREATE = (By.XPATH, '//li[contains(text(), "Logged as")]')
    TERM = (By.ID, 'term')
    CREATE_BUTTON = (By.ID, "submit")
    USER_EXIST = (By.XPATH, '//div[contains(text(), "User already exist")]')
    FLASH = (By.ID, 'flash')
    PASSWORD_ERROR = (By.XPATH, '//div[contains(text(), "Internal Server Error")]')
    ERROR_OF_LENTH = (By.XPATH, '//div[contains(text(), "Incorrect username length")]')
    ERROR_OF_MAIL = (By.XPATH, '//div[contains(text(), "Invalid email address")]')


class Main_locators:
    VERSION_BUTTON = (By.XPATH, '//a[contains(text(), " TM version 0.1")]')
    HOME_BUTTON = (By.LINK_TEXT, 'HOME')
    PYTHON_BUTTON = (By.LINK_TEXT, 'Python')
    PYTHON_HISTORY_BUTTON = (By.LINK_TEXT, 'Python history')
    LINUX_BUTTON = (By.LINK_TEXT, 'Linux')
    NETWORK_BUTTON = (By.LINK_TEXT, 'Network')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')
    LOAD_CENTOS = (By.XPATH, '//a[contains(text(), "Download Centos7")]')
    ABOUT_FLASK = (By.LINK_TEXT, 'About Flask')
    NEWS = (By.LINK_TEXT, 'NEWS')
    VK_ID = (By.XPATH, '//li[contains(text(), "VK ID:")]')
    DOWNLOAD_WIRESHARK = (By.LINK_TEXT, "DOWNLOAD")
    DOWNLOAD_SITE = (By.XPATH, '//strong[contains(text(), "Download Wireshark")]')
    EXAPMPLES = (By.XPATH, '//a[contains(text(), "Examples ")]')
    PICTURES = (By.XPATH, "//*[@class='uk-overlay uk-overlay-hover']")
    TEXT = (By.XPATH, '//h3[contains(text(), "Welcome to the TEST SERVER")]')
