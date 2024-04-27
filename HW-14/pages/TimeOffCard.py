from atf import *
from atf.ui import *
from controls import *
import datetime

from pages.StaffSelector import StaffSelector


@templatename('WorkTimeDocuments/timeoff:Dialog')
class TimeOffCard(DocumentTemplate):
    """Карточка отгула"""

    date = ControlsDatePickerOld(SabyBy.DATA_QA, 'wtd-DayTimeSelector__dateInput', 'Дата')
    choice_employee = ControlsLookupInput(rus_name='Сотрудник', catalog=StaffSelector)
    description = RichEditorExtendedEditor(SabyBy.DATA_QA, 'wtd-Base__comment', 'Описание')
    execute_btn = ControlsButton(By.CSS_SELECTOR, '.edo3-PassageButton', 'На выполнение')
    calendar = ControlsDatePopup()
    toolbar = ControlsToolbarsView()

    def fill_card_01(self, **kwargs):
        """Заполнить карточку (для теста 01)"""

        self.check_open()
        if 'Сотрудник' in kwargs.keys():
            self.choice_employee.autocomplete_search(kwargs['Сотрудник'])
        if 'Описание' in kwargs.keys():
            self.description.type_in(kwargs['Описание'])
        self.date.mouse_click()
        if 'Дата' in kwargs.keys():
            self.calendar.input_period(kwargs['Дата']).apply()
        if __name__ == 'test_02':
            pass

    def run_timeoff(self):
        """Запустить документ"""

        self.execute_btn.click()

    def close_timeoff(self):
        """Закрыть документ"""

        self.close()

    def check_data(self, **kwargs):
        """Проверить занчения в полях"""

        self.check_open()
        self.choice_employee.should_be(ContainsText(kwargs['Сотрудник']))
        self.description.should_be(ContainsText(kwargs['Описание']))
        self.date.mouse_click()
        self.calendar.start_date.should_be(ContainsText(kwargs['Дата'].strftime('%d.%m.%y')))

    def delete_timeoff(self):
        self.toolbar.select(data_qa='deleteDocument')
        self.popup_confirmation.confirm()
        self.check_close()
