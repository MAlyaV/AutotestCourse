# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("args, result, my_except", [
    ((10, 2), 5, None),
    ((7, 0), None, ZeroDivisionError),
    ((7, 4), 1.7, None),
    pytest.param((20, 4, '5', 1), None, TypeError, marks=pytest.mark.smoke),
    pytest.param((0, 7, 49), 0, None, marks=pytest.mark.skip(reason="Не тестируется"))

])
def test_all(args, result, my_except):
    if my_except is not None:
        with pytest.raises(my_except):
            assert all_division(*args) == result
    else:
        assert all_division(*args) == result
