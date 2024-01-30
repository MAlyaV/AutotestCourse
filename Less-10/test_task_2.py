# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_my_01():
    assert all_division(10, 2, 5) == 1


@pytest.mark.acceptance
def test_my_02():
    with pytest.raises(ZeroDivisionError):
        all_division(7, 0)


def test_03():
    assert all_division(7, 4) == 1.7


@pytest.mark.acceptance
def test_04():
    with pytest.raises(TypeError):
        all_division(20, 4, '5', 1)


@pytest.mark.smoke
@pytest.mark.acceptance
def test_05():
    assert all_division(0, 7, 49) == 0
