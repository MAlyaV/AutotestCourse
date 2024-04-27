from atf import *
from atf.ui import *
from controls import *


class Documents(Region):
    """Реестр документов"""

    create_dwbtn = ExtControlsDropdownAddButton()
    documents_list = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="wtd-List"]', 'Список документов')

    def open_page(self):
        log('Переход в реестр "Документы"')
        self.browser.open(self.config.get('SITE_TASK'))
        self.check_page_load_wasaby()

    def create_timeoff(self):
        log('Создание отгула')
        from pages.TimeOffCard import TimeOffCard

        self.create_dwbtn.select('Time off', 'Time off')
        card = TimeOffCard(self.driver)
        card.check_open()
        return card

    def check_timeoff(self, **kwargs):
        log('Проверка наличия в реестре')
        self.documents_list.row(contains_text=kwargs['Описание']).should_be(Displayed)

    def open_timeoff(self, **kwargs):
        log('Открытие документа из реестра')
        self.documents_list.row(contains_text=kwargs['Описание']).click()
