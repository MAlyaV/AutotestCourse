# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

driver = webdriver.Chrome()

try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    driver.get('https://fix-online.sbis.ru/')
    sleep(2)
    user_login, user_password = 'fford', 'ASD123'
    login = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] input')
    login.send_keys(user_login, Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '.auth-AdaptiveLoginForm__password input')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    # Перейти в реестр Контакты
    contacts = driver.find_element(By.CSS_SELECTOR, 'a[data-qa="Contacts"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(contacts)
    action_chains.double_click(on_element = contacts)
    action_chains.perform()
    sleep(2)

    dialogs_page = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Tabs__item-element"] [href="/page/dialogs"]')
    dialogs_page.click()

    # Отправить сообщение самому себе
    plus = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus.click()
    sleep(2)

    # В поле поиска вбить свою фамилию
    user_name = 'Ford David'
    search = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] input')
    search.send_keys(user_name)
    sleep(3)
    # Выбрать пользователя для отправки сообщения
    person_choice = driver.find_element(By.CSS_SELECTOR, '.controls-ListView__itemContent '
                                                         '.msg-addressee-selector__addressee')
    person_choice.click()
    sleep(2)
    # Написать и отправить
    message = 'Сообщение для пользователя Ford David:\nПривет!'
    field = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    field.send_keys(message, Keys.CONTROL + Keys.ENTER)
    close = driver.find_element(By.CSS_SELECTOR, '.icon-Close')
    close.click()
    sleep(2)

    # Убедиться, что сообщение появилось в реестре
    my_message = driver.find_element(By.XPATH, '//div[@data-qa="list"]//div[1][@data-qa="item"]//div[@class]//p')
    assert my_message.text == 'Сообщение для пользователя Ford David:', 'Сообщение не найдено'

    # Удалить это сообщение и убедиться, что удалили
    message_block = driver.find_element(By.XPATH, '//div[@data-qa="list"]//div[1][@data-qa="item"]')
    action_chains.move_to_element(my_message)
    action_chains.context_click(my_message)
    action_chains.perform()
    sleep(2)
    delete = driver.find_element(By.CSS_SELECTOR, '[title="Move to deleted"]')
    delete.click()
    message_block_new = driver.find_element(By.XPATH, '//div[@data-qa="list"]//div[1][@data-qa="item"]')
    assert message_block_new.text[:11:] != ' Ford David', 'Сообщение не удалено'
    sleep(2)
finally:
    driver.quit()
