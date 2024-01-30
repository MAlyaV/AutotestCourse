import pytest
import time


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    start_time = time.time()

    def result():
        end_time = time.time()
        print(f"\nВсе тесты класса выполнились за {end_time - start_time} секунд.")

    return result()


@pytest.fixture
def test_fixture():
    start_time = time.time()

    def result():
        end_time = time.time()
        print(f"\nТест выполнился за {end_time - start_time} секунд.")

    return result()
