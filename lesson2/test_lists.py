def test_list_empty(create_simple_list):
    """создание пустого списка"""
    list_two = []
    assert create_simple_list == list_two


def test_empty_list_vs_full_list(create_simple_list):
    """"сравнение пустого и заполненного списка"""
    list_two = [1]
    assert create_simple_list != list_two


def test_not_equal_value(create_list_with_value):
    """"Сравнение списков с разными значениями"""
    list_with_value_one = [2]
    assert list_with_value_one != create_list_with_value


def test_length_of_list():
    """Проверка длинны списка"""
    list_contains = [1, 2, 3]
    assert len(list_contains) == 3


def test_value_is_equal(one_name_of_list):
    assert one_name_of_list == 'Andrey' or 'Ivan' or 'Tanya'

