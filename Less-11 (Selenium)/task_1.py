# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
try:
    # Перейти на https://sbis.ru/

    driver.get('https://sbis.ru/')
    sleep(2)

    # Перейти в раздел "Контакты"

    contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts_btn.click()
    sleep(2)

    # Найти баннер Тензор, кликнуть по нему
    # Перейти на https://tensor.ru/

    tensor_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    tensor_btn.click()
    sleep(2)

    # Проверить, что есть блок новости "Сила в людях"

    driver.switch_to.window(driver.window_handles[1])
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    assert news_block.is_displayed(), 'Блок новости "Сила в людях" не найден'

    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about

    detail_news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    #Скролл к нужному элементу
    detail_news_block.location_once_scrolled_into_view
    sleep(2)
    detail_news_block.click()
    sleep(2)
    assert driver.current_url == 'https://tensor.ru/about', 'Неверно открыт сайт'
finally:
    driver.quit()