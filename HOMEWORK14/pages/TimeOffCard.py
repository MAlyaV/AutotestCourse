from atf.ui import *
from controls import *

from CourseAutotests.HOMEWORK14.pages.StaffSelector import StaffSelector


@templatename('WorkTimeDocuments/timeoff:Dialog')
class TimeOffCard(DocumentTemplate):
    """Карточка отгула"""

    date = ControlsDatePickerOld(SabyBy.DATA_QA, 'wtd-DayTimeSelector__dateInput', 'Дата')
    choice_employee = ControlsLookupInput(rus_name='Сотрудник', catalog=StaffSelector)
    description = RichEditorExtendedEditor(SabyBy.DATA_QA, 'wtd-Base__comment', 'Описание')
    execute_btn = ControlsButton(By.CSS_SELECTOR, '.edo3-PassageButton', 'На выполнение')
    calendar = ControlsDatePopup()
    toolbar = ControlsToolbarsView()
    save_btn = ControlsButton(SabyBy.DATA_QA, 'extControls-singleButton__icon', 'Сохранить')
    time_icon = Element(By.CSS_SELECTOR, '.icon-TimeSkinny', 'Время')
    start_time_input = ControlsInputMask(By.CSS_SELECTOR, '[data-qa="wtd-TimeIntervalMinutes__start"]', 'Время начала')
    end_time_input = ControlsInputMask(By.CSS_SELECTOR, '[data-qa="wtd-TimeIntervalMinutes__end"]', 'Время окончания')

    def fill_card(self, timeoff_time, **kwargs):
        """Заполнить карточку"""

        self.check_open()
        if 'Сотрудник' in kwargs.keys():
            self.choice_employee.autocomplete_search(kwargs['Сотрудник'])
        if 'Описание' in kwargs.keys():
            self.description.type_in(kwargs['Описание'])
        self.date.mouse_click()
        if 'Дата' in kwargs.keys():
            self.calendar.input_period(kwargs['Дата']).apply()
        if timeoff_time:
            if 'Время отгула' in kwargs.keys():
                self.time_icon.click()
                self.start_time_input.type_in(kwargs['Время отгула'][0], clear_txt=False)
                self.end_time_input.type_in(kwargs['Время отгула'][1], clear_txt=False)

    def save_timeoff(self):
        """Сохранить отгул"""
        self.save_btn.click()

    def check_data(self, **kwargs):
        """Проверить занчения в полях"""

        self.check_open()
        self.choice_employee.should_be(ContainsText(kwargs['Сотрудник']))
        self.description.should_be(ContainsText(kwargs['Описание']))
        self.date.mouse_click()
        self.calendar.start_date.should_be(ContainsText(kwargs['Дата'].strftime('%d.%m.%y')))
        if self.start_time_input.is_displayed:
            self.start_time_input.should_be(ContainsText(kwargs['Время отгула'][0]))
            self.end_time_input.should_be(ContainsText(kwargs['Время отгула'][1]))

    def delete_timeoff(self):
        """Удалить отгул"""
        self.toolbar.select(data_qa='deleteDocument')
        self.popup_confirmation.confirm()
        self.check_close()
