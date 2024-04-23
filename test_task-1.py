from atf import log
from atf.ui import *
from controls import *
from pages.auth_page import AuthPage
from pages.contacts_page import TaskContacts


class TestContactsTask(TestCaseUI):
    message_text = 'АВТОТЕСТЫ. Less -13'

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.page = TaskContacts(cls.driver)

    def setUp(self):
        self.page.check_load()

    @classmethod
    def teardown_method(self):
        self.browser.open(self.config.get('SITE_TASK'))

    def test_01_check_messages(self, message_text=message_text):
        """Переместить запись в другую папку и проверить перемещение (убедиться в: наличии в папке и увеличении
        счётчика).Вернуть обратно. """

        folder_name = 'Другая папка'

        log('Переместить запись в другую папку')
        self.page.move_message(message=message_text, folder=folder_name)

        log('Проверить перемещение и вернуть сообщение обратно')
        self.page.check_message(message=message_text, folder=folder_name)

    def test_02_check_counters(self, message_text=message_text):
        """Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах"""

        message_date = '17 апр 16:47'

        self.page.check_message_date(message=message_text, date=message_date)

    def test_03_check_tag(self, message_text=message_text):
        tag_text = 'Для АТ'

        """Пометить сообщение эталонным тегом"""
        self.page.add_tag(message=message_text, tag=tag_text)

        """Убедиться, что тег появился на сообщении, а счётчик тегов увеличился"""
        self.page.check_tag(message=message_text, tag=tag_text)

        """Снять тег и проверить"""
        self.page.reset_tag(message=message_text, tag=tag_text)
