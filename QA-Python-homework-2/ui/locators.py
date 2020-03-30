from selenium.webdriver.common.by import By


class Auth_Locators:
    ENTER_BUTTON = (By.CLASS_NAME, "responseHead-module-button-1BMAy4")
    EMAIL_LOCATION = (By.NAME, "email")
    PASSWORD_LOCATION = (By.NAME, "password")
    CHECK_LOCATION = (By.CLASS_NAME, "right-module-userNameWrap-34ibLS")
    CHECK_FAIL = (By.CLASS_NAME, "formMsg_title")


class Main_Locators:
    LINK_CREATE_COMPANY = (By.XPATH, '//span[contains(@data-loc-ru, "Создать кампанию")]')
    LINK_ZERO_COMPANY = (By.PARTIAL_LINK_TEXT, 'создайте')
    TYPE_OF_COMPANY = (By.XPATH, '//div[contains(text(), "Охват")]')
    LINK_FIELD = (By.XPATH, '//input[contains(@class, "input__inp js-form-element")]')
    NAME_FIELD = (By.XPATH, '(//input[contains(@class, "input__inp js-form-element")])[2]')
    DOWNLOAD_ELEMENT = (By.XPATH, '//input[contains(@class, "input__inp input__inp_file js-form-element")]')
    BANNER = (By.ID, '192')
    BUTTON_CREATE_COMPANY = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    LINK_COMPANY = (By.XPATH, '//a[contains(@class, "campaigns-tbl-cell__campaign-name")]')

    BUTTON_AUDITORIUM = (By.XPATH, '//a[contains(@href, "/segments")]')
    LINK_ZERO_AUDITORIUM = (By.PARTIAL_LINK_TEXT, 'Создайте')
    LINK_CREATE_AUDITORIUM = (By.XPATH, '//div[contains(@class, "button__text")]')
    ADD_SEGMENTS = (By.XPATH, '//span[contains(@data-loc-ru, "Добавить аудиторные сегменты...")]')
    NAME_SEGMENT_FIELD = (By.XPATH, '(//input[contains(@class, "input__inp js-form-element")])[2]')
    OPTION_SEGMENT = (By.XPATH, '//div[contains(text(), "Приложения (ОК и МойМир)")]')
    FIRST_CHECKBOX =(By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox js-main-source-checkbox")]')
    SECOND_CHECKBOX = (By.XPATH, '//input[contains(@class, "segment-settings-view__checkbox js-payer-checkbox-pay")]')
    BUTTON_OPTION = (By.XPATH, '//span[contains(text(), "Игравшие и платившие в платформе")]')
    BUTTON_CREATE_OPTION = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    CREATE_SEGMENT = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    CLICK_ELEMENT = (By.XPATH, '//span[contains(@class, "adv-camp-cell adv-camp-cell_name")]')
    CHECK_ELEMENT = (By.XPATH, '//a[contains(@class, "adv-camp-cell adv-camp-cell_name")]')
    DELETE_ELEMENT = (By.XPATH, '//div[contains(@class, "remove-source-wrap js-remove-source")]')
    DELETE_BUTTON = (By.XPATH, '//div[contains(text(), "Удалить")]')
