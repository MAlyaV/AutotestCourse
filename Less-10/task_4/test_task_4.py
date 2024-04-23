# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


class TestClass:
    @pytest.mark.usefixtures("class_fixture")
    def test_1(self, test_fixture):
        assert 1 == 1

    @pytest.mark.usefixtures("class_fixture")
    def test_2(self, test_fixture):
        assert 2 == 2

    def test_3(self):
        assert 3 == 3
