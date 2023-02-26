import pytest
from unittest import TestCase
from tasks import getting_new_list, unique_values, get_most_pop_comp, stats

# Тестирование задания 1
def test_1():
    res = getting_new_list()
    res_expected = [{'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}]
    assert isinstance(res, list), 'Значение должно быть листом'
    assert res == res_expected

# Тестирование задания 2
class Test(TestCase):
    def test_class(self):
        result = unique_values()
        self.assertIsInstance(result, list)


def test_2():
    res = unique_values()
    assert isinstance(res, list)
    res_expected = [98, 35, 15, 213, 54, 119]
    assert res == res_expected

# Тестирование задания 3

def test_3():
    res = get_most_pop_comp()
    assert res == 'yandex', 'Значение должно быть - yandex'
    def testing_func():
        for keys, values in stats.items():
            if values == max(stats.values()):
                return keys
    assert res == testing_func(), 'Значение должно быть наибольшим'
    assert isinstance(res, str), 'На выходе должна быть строка'
    




