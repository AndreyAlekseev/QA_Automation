def test_create_new_dict():
    """Create empty dict"""
    new_dict = {}
    assert type(new_dict) == dict


def test_dict_with_elements(create_dict_with_value):
    """"Create filled dictionary"""
    new_dict = create_dict_with_value
    new_dict2 = {'Value1': 1, 'Value2': 2}
    assert new_dict == new_dict2 and type(new_dict) == dict


def test_update_some_element(create_dict_with_value):
    """Update 1st element"""
    new_dict = create_dict_with_value
    new_dict2 = new_dict.copy()
    new_dict2['Value1'] = 2
    assert new_dict != new_dict2


def test_delete_some_element(create_dict_with_value):
    """"Delete last element"""
    new_dict = create_dict_with_value
    new_dict2 = new_dict.copy()
    new_dict2.popitem()
    assert new_dict != new_dict2


def test_added_some_element(create_dict_with_value):
    """"Add some element"""
    new_dict = create_dict_with_value
    new_dict2 = new_dict.copy()
    new_dict['Value3'] = 3
    assert new_dict != new_dict2

