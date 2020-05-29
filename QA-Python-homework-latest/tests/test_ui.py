from base_case import BaseCase, BaseCaseCreate, BaseCaseMain
import pytest
import allure
import selenium
import datetime


class Test_UI_Auth(BaseCase):
    @allure.story('main')
    @pytest.mark.main
    def test_exist(self):
        """Проверка грузится ли стартовая страница приложения"""
        check = self.page.find(self.page.locators.TEXT)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/Server',
                      attachment_type=allure.attachment_type.PNG)
        assert check is not None

    @allure.story('main')
    @pytest.mark.main
    def test_positive_auth(self, auth_data):
        """Проверка проходит ли аутентификация если данные заранее есть"""
        self.page.auth(auth_data['user'], auth_data['password'])
        check = self.page.find(self.page.locators.ACCESS_AUTH)
        assert check.text.split()[-1] == auth_data['user']

    @allure.story('other')
    @pytest.mark.other
    def test_without_ID(self, delete_id, second_auth_data):
        self.page.auth(*second_auth_data)
        self.page.click(self.page.locators.HOME_BUTTON)
        with pytest.raises(selenium.common.exceptions.TimeoutException):
            self.page.find(self.page.locators.VK_ID, timeout=1)

    @allure.story('main')
    @pytest.mark.main
    def test_fail_auth(self, auth_data):
        """Проверка что аутентификация не пройдет при верном пользователе
        и кривом пароле"""
        self.page.auth(auth_data['user'], '42')
        check = self.page.find(self.page.locators.FLASH)
        print(check.text)
        assert check.text == 'Invalid username or password'

    @allure.story('main')
    @pytest.mark.main
    def test_void_data(self):
        """Проверка, что аутентификация с пустыми полями провалится"""
        self.page.click(self.page.locators.LOGIN_BUTTON)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        check = self.page.find(self.page.locators.TEXT)
        assert check is not None

    @allure.story('main')
    @pytest.mark.main
    def test_void_password(self, auth_data):
        """Проверка, что аутентификация с пустым полем пароля провалится"""
        self.page.completion(auth_data['user'], self.page.locators.USER_FIELD)
        self.page.click(self.page.locators.LOGIN_BUTTON)
        check = self.page.find(self.page.locators.TEXT)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_hell_user_auth(self):
        """Проверка, что при входе с невозможно длинным паролем приложение
        реагирует корректно"""
        self.page.auth(256 * 'a', '1234')
        check = self.page.find(self.page.locators.USER_LENTH_ERROR)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_ban_auth(self):
        """Проверка, что заблокированный пользователь не пройдет
        аутентификацию"""
        self.page.auth('ban_user', '123456')
        check = self.page.find(self.page.locators.BAN_AUTH)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/Ban',
                      attachment_type=allure.attachment_type.PNG)
        assert check is not None

    @allure.story('main')
    @pytest.mark.main
    def test_to_create(self):
        """Проверка, что переход на страницу создания пользователя по ссылке
        снизу происходит корректно"""
        self.page.to_create()
        check = self.page.find(self.page.locators.CREATE_TEXT)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_active_when_lock(self, special_user, sql_client, norm_auth):
        """Проверка изменится ли active при блокировке пользователя"""
        norm_auth.unlock(special_user[0])
        self.page.auth(*special_user)
        norm_auth.lock(special_user[0])
        assert sql_client.select('username', special_user[0])[0][5] == 0


class Test_UI_Create(BaseCaseCreate):
    @allure.story('main')
    @pytest.mark.main
    def test_to_auth(self):
        """Проверка, что переход на страницу аутентификации по ссылке
        снизу происходит корректно"""
        self.page.to_auth()
        check = self.page.find(self.page.locators.TEXT)
        assert check is not None

    @allure.story('main')
    @pytest.mark.main
    def test_create(self, data_to_create, sql_client):
        """Проверка, что создание при "здоровых" данных проходит успешно
        и происходит переход на главную страницу"""
        self.page.create_user(data_to_create['user'], data_to_create['email'],
                              data_to_create['password'])
        check = self.page.find(self.page.locators.ACCESS_CREATE)
        sql_data = sql_client.select('username', data_to_create['user'])
        assert sql_data[0][2] == data_to_create['password']
        assert check.text.split()[-1] == data_to_create['user']

    @allure.story('other')
    @pytest.mark.other
    def test_create_invalid_user(self, data_to_create):
        """Проверка, что при создании при невозможной длине пользователя
        приложение реагирует корректно"""
        self.page.create_user("w" * 17, data_to_create['email'],
                              data_to_create['password'])
        check = self.page.find(self.page.locators.ERROR_OF_LENTH)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_create_invalid_mail(self, data_to_create):
        """Проверка, что при создании при невозможном майле приложение
        реагирует корректно"""
        self.page.create_user(data_to_create['user'], "qwerty",
                              data_to_create['password'])
        check = self.page.find(self.page.locators.ERROR_OF_MAIL)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_create_exist_name(self, data_to_create):
        """Проверка, что при создании пользователя с существующим именем
        приложение реагирует корректно"""
        self.page.create_user("enter_user", data_to_create['email'],
                              data_to_create['password'])
        check = self.page.find(self.page.locators.USER_EXIST)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_create_with_space(self, data_to_create, date_with_space):
        """Проверка, что нельзя создать пользователя с 7 пробелами в центре"""
        self.page.create_user(date_with_space, data_to_create['email'],
                              data_to_create['password'])
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='/screenshort/user_with_space',
                      attachment_type=allure.attachment_type.PNG)
        check = self.page.find(self.page.locators.USER_FIELD, timeout=1)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_create_exist_email(self, data_to_create):
        """Проверка, что при создании пользователя с существующим email
        приложение реагирует корректно"""
        self.page.create_user(data_to_create['user'], 'a@m.ru',
                              data_to_create['password'])
        check = self.page.find(self.page.locators.FLASH)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='/screenshort/email',
                      attachment_type=allure.attachment_type.PNG)
        assert check.text != 'Internal Server Error'

    @allure.story('other')
    @pytest.mark.other
    def test_create_hell_password(self, data_to_create):
        """Проверка, что при создании пользователя с невозможно длинным паролем
        приложение реагирует корректно"""
        self.page.create_user(data_to_create['user'], data_to_create['email'],
                              'a' * 256)
        check = self.page.find(self.page.locators.PASSWORD_ERROR)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='/screenshort/password',
                      attachment_type=allure.attachment_type.PNG)
        assert check.text != 'Internal Server Error'

    @allure.story('other')
    @pytest.mark.other
    def test_two_create_errors(self):
        """Проверка, что с двумя некорректно заполненными полями приложение
        корректно пишет ошибку"""
        self.page.create_user('q' * 17, 'q' * 5, '123456')
        check = self.page.find(self.page.locators.ERROR_OF_LENTH)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='/screenshort/two_errors',
                      attachment_type=allure.attachment_type.PNG)
        assert check.text == 'Incorrect username length\nInvalid email address'

    @allure.story('other')
    @pytest.mark.other
    def test_start_active_time_create(self, sql_client, data_to_create):
        """Проверка, что start_active_time проставляется при первом входе
        при создании"""
        self.page.create_user(data_to_create['user'], data_to_create['email'],
                              data_to_create['password'])
        start_time = sql_client.select('username', data_to_create['user'])[0][6]
        assert start_time.hour + 3 == datetime.datetime.now().hour
        assert start_time.minute == datetime.datetime.now().minute


class Test_UI_Main(BaseCaseMain):
    @allure.story('other')
    @pytest.mark.other
    def test_version_button(self):
        """Проверка, что при нажатии на кнопку версии страница обновится"""
        self.page.click(self.page.locators.VERSION_BUTTON)
        check = self.page.find(self.page.locators.HOME_BUTTON)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_home_button(self):
        """Проверка, что при нажатии на кнопку HOME страница обновится"""
        self.page.click(self.page.locators.HOME_BUTTON)
        check = self.page.find(self.page.locators.VERSION_BUTTON)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_python_button(self):
        """Проверка, что при нажатии на кнопку PYTHON откроется python.org"""
        self.page.click(self.page.locators.PYTHON_BUTTON)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/Python',
                      attachment_type=allure.attachment_type.PNG)
        assert self.page.driver.title == "Welcome to Python.org"

    @allure.story('other')
    @pytest.mark.other
    def test_python_history_button(self):
        """Проверка, что при нажатии на кнопку Python history
        откроется история python"""
        self.page.move_to(self.page.locators.PYTHON_BUTTON)
        self.page.click(self.page.locators.PYTHON_HISTORY_BUTTON)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/Python_history',
                      attachment_type=allure.attachment_type.PNG)
        assert "History of Python" in self.page.driver.title

    @allure.story('other')
    @pytest.mark.other
    def test_centos_button(self):
        """Проверка, что кнопка загрузки centos ведет на сайт загрузки"""
        main_handle = self.page.driver.window_handles[0]
        self.page.move_to(self.page.locators.LINUX_BUTTON)
        self.page.click(self.page.locators.LOAD_CENTOS)
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/CentOs7',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert "CentOs" in title

    @allure.story('other')
    @pytest.mark.other
    def test_about_flask_button(self):
        """Проверка, что кнопка about flask ведет на сайт о Flask"""
        main_handle = self.page.driver.window_handles[0]
        self.page.move_to(self.page.locators.PYTHON_BUTTON)
        self.page.click(self.page.locators.ABOUT_FLASK)
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/Flask',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert "Welcome to Flask" in title

    @allure.story('other')
    @pytest.mark.other
    def test_news_button(self):
        """Проверка, что кнопка News wireshark ведет на сайт с
        новостями о wireshark"""
        main_handle = self.page.driver.window_handles[0]
        self.page.move_to(self.page.locators.NETWORK_BUTTON)
        self.page.click(self.page.locators.NEWS)
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert "News" in title

    @allure.story('other')
    @pytest.mark.other
    def test_download_button(self):
        """Проверка, что кнопка Download wireshark ведет на сайт с
        загрузкой wireshark"""
        main_handle = self.page.driver.window_handles[0]
        self.page.move_to(self.page.locators.NETWORK_BUTTON)
        self.page.click(self.page.locators.DOWNLOAD_WIRESHARK)
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        check = self.page.find(self.page.locators.DOWNLOAD_SITE)
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_exaples_button(self):
        """Проверка, что кнопка Examples Tcpdumps ведет на сайт с
        примерами TCPdumps"""
        main_handle = self.page.driver.window_handles[0]
        self.page.move_to(self.page.locators.NETWORK_BUTTON)
        self.page.click(self.page.locators.EXAPMPLES)
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert 'Tcpdump Examples' in title

    @allure.story('other')
    @pytest.mark.other
    def test_api_button(self):
        """Проверка, что кнопка about Api ведет на сайт о API"""
        main_handle = self.page.driver.window_handles[0]
        element = self.page.driver.find_elements(*self.page.locators.PICTURES)[0]
        element.click()
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert 'Application programming interface' in title

    @allure.story('other')
    @pytest.mark.other
    def test_future_button(self):
        """Проверка, что кнопка Future of internet ведет на сайт о
        будущем интернета"""
        main_handle = self.page.driver.window_handles[0]
        element = self.page.driver.find_elements(*self.page.locators.PICTURES)[1]
        element.click()
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert 'Next 50 Years' in title

    @allure.story('other')
    @pytest.mark.other
    def test_smtp_button(self):
        """Проверка, что кнопка Lets talk about SMTP ведет на сайт о
        SMTP"""
        main_handle = self.page.driver.window_handles[0]
        element = self.page.driver.find_elements(*self.page.locators.PICTURES)[2]
        element.click()
        handle = self.page.driver.window_handles
        self.page.driver.switch_to.window(handle[1])
        title = self.page.driver.title
        allure.attach(self.page.driver.get_screenshot_as_png(),
                      name='./screenshort/News',
                      attachment_type=allure.attachment_type.PNG)
        self.page.driver.close()
        self.page.driver.switch_to.window(main_handle)
        assert 'SMTP' in title

    @allure.story('other')
    @pytest.mark.other
    def test_VK_ID(self, get_id):
        """Проверка, что если у пользователя есть VK_ID, то этот id
        выведется"""
        self.page.click(self.page.locators.HOME_BUTTON)
        assert self.page.find(self.page.locators.VK_ID).text == f'VK ID: {get_id["vk_id"]}'

    @allure.story('other')
    @pytest.mark.other
    def test_start_active_time_auth(self, sql_client, auth_data):
        """Проверка, что start_active_time обновляется на время входа при
        аутентификации"""
        start_time = sql_client.select('username', auth_data['user'])[0][6]
        assert start_time.hour + 3 == datetime.datetime.now().hour
        assert start_time.minute == datetime.datetime.now().minute

    @allure.story('other')
    @pytest.mark.other
    def test_logout(self):
        """Проверка, что logout разлогинивает пользователя"""
        self.page.click(self.page.locators.LOGOUT_BUTTON)
        check = self.page.find(self.page.locators.TEXT)
        assert check is not None

    @allure.story('other')
    @pytest.mark.other
    def test_active_logout(self, sql_client, auth_data):
        """Проверка, что active ставится в 0 при нажатии на logout"""
        self.page.click(self.page.locators.LOGOUT_BUTTON)
        assert sql_client.select('username', auth_data['user'])[0][5] == 0
