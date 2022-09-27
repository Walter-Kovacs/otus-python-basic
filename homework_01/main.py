"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n ** 2 for n in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number == 0 or number == 1:
        return False

    n = 2
    while n ** 2 <= number:
        if number % n == 0:
            return False
        n += 1

    return True


def filter_numbers(list_of_numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 == 1, list_of_numbers))
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, list_of_numbers))
    if filter_type == PRIME:
        return list(filter(is_prime, list_of_numbers))
