from atf.ui import *
from controls import *


class TaskContacts(Region):
    """Реестр Контактов"""

    messages = ControlsListView(By.CSS_SELECTOR, '.msg-dialogs-detail [data-qa="items-container"]', 'Сообщения')
    move_button = ControlsOperationsPanel(By.CSS_SELECTOR, '[data-qa="move"]', 'Переместить')
    move_dialog = ControlsMoveDialog()
    folders = ControlsTreeGridView()
    messages_counter = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="msg-folders-counter_total"]', 'Счётчик папки')
    tabs_buttons = ControlsTabsButtons()
    chats = ControlsListView(By.CSS_SELECTOR, '.msg-CorrespondenceDetail [data-qa="items-container"]', 'Чаты')
    dropdown_popup = ControlsPopup()
    tag_popup = ControlsListView(By.CSS_SELECTOR, '.controls-Popup .controls-ListViewV', 'Окно выбора тега')
    # message_tag = ControlsListView(By.CSS_SELECTOR, '.controls-ListViewV .msg-dialogs-item__tags', 'Теги сообщения')
    tag_list = ControlsListView(By.CSS_SELECTOR, '.msg-tag-list .controls-ListViewV', 'Список тегов')

    # tag_list_counter = ControlsListView(By.CSS_SELECTOR, '.tags-base__counter', 'Счетчик тега')

    def check_load(self):
        """Проверка звгрузки реестра"""

        self.folders.check_load()
        self.messages.check_load()

    def move_message(self, message, folder):
        """"Перемещение сообщения"""

        self.messages.item(self, contains_text=message).should_be(Displayed)
        self.messages.select_key_space(self, contains_text=message)
        self.move_button.click()
        self.move_dialog.select(contains_text=folder)

    def check_message(self, folder, message):
        """Проверка перемещения"""

        self.messages_counter.should_be(ExactText('1'))
        self.folders.row(contains_text=folder).click()
        self.messages.item(self, contains_text=message).should_be(Displayed)

        """Возврат сообщения"""
        self.messages.select_key_space(self, contains_text=message)
        self.move_button.click()
        self.move_dialog.select(contains_text='Все сообщения')
        self.messages_counter.should_not_be(Displayed)

    def check_message_date(self, message, date):
        """Проверка даты сообщения в Диалогах и Чатах"""
        self.messages.item(self, contains_text=message).should_be(ContainsText(date))
        self.tabs_buttons.select(title="Чаты").click()
        self.chats.item(self, contains_text=message).should_be(ContainsText(date))

    def add_tag(self, message, tag):
        """Установка тега"""
        self.messages.item(self, contains_text=message).should_be(Displayed).context_click()
        self.dropdown_popup.get_item_by_text('Пометить').click()
        self.tag_popup.item(self, contains_text=tag).should_be(Displayed).click()

    def check_tag(self, message, tag):
        """Проверка тега на сообщении и счётчика"""
        self.messages.item(self, contains_text=message).element(
            '.controls-ListViewV .msg-dialogs-item__tags').should_be(ExactText('Для АТ'))
        self.tag_list.item(self, contains_text=tag).element('.tags-base__counter').should_be(ExactText('1'))

    def reset_tag(self, message, tag):
        """Сброс тега"""
        self.messages.item(self, contains_text=message).element('.tags-base__close').click()
        self.messages.item(self, contains_text=message).should_not_be(ContainsText(tag))
        self.tag_list.item(self, contains_text=tag).element('.tags-base__counter').should_not_be(Displayed)
