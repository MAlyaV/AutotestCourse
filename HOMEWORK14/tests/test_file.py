import datetime
from atf import *
from atf.ui import *
import inspect

from CourseAutotests.HOMEWORK14.pages.AuthPage import AuthPage
from CourseAutotests.HOMEWORK14.pages.Documents import Documents


class TestTimeOff(TestCaseUI):
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    timeoff_data = {'Сотрудник': 'Чернов Лев', 'Описание': 'Для АТ\n*Сотрудник усталь...)', 'Дата': tomorrow,
                    'Время отгула': ['12:00', '14:00']}
    timeoff_time = False

    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        Documents(self.driver).open_page()

    def timeoff_actions(self):
        # Проверяем, откуда вызван метод
        if inspect.currentframe().f_back.f_code.co_name == 'test_02':
            self.timeoff_time = True
        task_page = Documents(self.driver)
        timeoff_card = task_page.create_timeoff()
        timeoff_card.fill_card(self.timeoff_time, **self.timeoff_data)
        timeoff_card.save_timeoff()
        self.browser.refresh()
        task_page.check_timeoff(**self.timeoff_data)
        task_page.open_timeoff(**self.timeoff_data)
        timeoff_card.check_data(**self.timeoff_data)
        timeoff_card.delete_timeoff()

    def test_01(self):
        """
        Создать отгул
        Выбрать сотрудника через автодополнение, которому создаем отгул
        Выставить дату - завтра
        Заполнить причину
        Запустить в ДО
        Убедиться, что появился в реестре и при переоткрытии значения в полях сохранились
        Удалить отгул
        """

        self.timeoff_actions()

    def test_02(self):
        """
        Создать отгул
        Выбрать сотрудника через справочник
        Выставить время завтра с 12 до 14 часов
        Заполнить описание
        Сохранить
        Убедиться, что появился в реестре и при переоткрытии значения в полях сохранились
        Удалить отгул
        """

        self.timeoff_actions()
