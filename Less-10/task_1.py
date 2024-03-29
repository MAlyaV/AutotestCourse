# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name():
    while True:

        word1 = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 15)))
        word2 = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 15)))

        yield f"{word1} {word2}"


# Пример использования
gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



