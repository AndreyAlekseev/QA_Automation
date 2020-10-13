import pytest


def test_create_empty_set():
    """создание пустого множества"""
    set1 = set()
    assert type(set1) == set


def test_create_set_with_value():
    """создание множество с значением"""
    set1 = {1, 2, 3}
    assert set1 is not None


def test_add_value_in_set():
    """добавление значения в существующее множество"""
    set1 = {1, 3, 4}
    set1.add(9)
    assert 9 in set1


def test_remove_element_from_set():
    """удаление одного элемента из множества"""
    set1 = {1, 2, 3}
    set1.remove(2)
    assert 2 not in set1


@pytest.mark.parametrize("test_value", [(1, 'Egor')])
def test_any_type_args_in_set(test_value):
    """содержание разных типов в множестве"""
    set1 = set(test_value)
    set2 = set({1, 'Egor'})
    assert set1 == set2
