def test_create_string():
    """"Create string"""
    name = 'Boris'
    assert type(name) == str


def test_concat_some_symbol():
    """"Concat some value to string"""
    name = 'Ivan'
    last_name = ' Drago'
    full_name = name + last_name
    assert full_name == 'Ivan Drago'


def test_change_some_type_to_string(create_list_with_value):
    """"Change list to str"""
    string = (" ".join(map(str, create_list_with_value)))
    assert type(string) == str


def test_sum_int_vs_string():
    """"Change type int to str and use to result"""
    one = 1
    two = '2'
    result = str(one) + two
    assert result == str(12)


def test_numbers_of_letters():
    """"Numbers of letter"""
    name = 'Donald'
    res = len(name)
    assert res == 6


