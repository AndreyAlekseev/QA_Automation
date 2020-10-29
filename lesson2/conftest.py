import pytest


@pytest.fixture()
def create_simple_list():
    list_one = []
    return list_one


@pytest.fixture()
def create_list_with_value():
    list_with_value = [1]
    return list_with_value


@pytest.fixture(params=[('Andrey', 'Ivan', 'Tanya')])
def one_name_of_list(request):
    return request.param


@pytest.fixture(params=[{'Value1': 1, 'Value2': 2}])
def create_dict_with_value(request):
    return request.param
