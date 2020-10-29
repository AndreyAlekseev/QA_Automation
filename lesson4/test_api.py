import pytest
import requests
import json
from jsonschema import validate

TODOS_MAX = 200
USERID = 10


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    yield validate(instance=data, schema=schema)
    f.close()


def test_getting_a_resource(session, base_url):
    """"get status 200"""
    res = session.get(url=f'{base_url}/1')
    assert_valid_schema(res.json(), 'schemas/todos_schema.json')
    assert res.status_code == 200


@pytest.mark.parametrize('todos_userId', [-1, 0, TODOS_MAX + 1])
def test_getting_a_resource_negative(session, base_url, todos_userId):
    """"get status 404 with not valid params"""
    res = session.get(url=f'{base_url}/{todos_userId}')
    assert res.status_code == 404
    assert not res.json()


@pytest.mark.parametrize('empty_arr', [[], [1], ['s'], [object]])
def test_get_empty_arr(session, base_url, empty_arr):
    """"get status 404 with empty list"""
    res = session.get(url=f'{base_url}/{empty_arr}')
    assert res.status_code == 404
    assert not res.json()


def test_listing_all_resources(session, base_url):
    """"listing first, central, last item"""
    res = session.get(url=f'{base_url}')
    assert_valid_schema(res.json(), 'schemas/todos_all_items_schema.json')
    assert res.status_code == 200


def test_creating_a_resource(session, base_url):
    """"Create new item"""
    userId = 11
    id = 201
    title = "Euro training!"
    payload = {'userId': userId, 'id': id, 'title': title}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 201
    j = res.json()
    assert j['userId'] == USERID + 1
    assert j['id'] == TODOS_MAX + 1
    assert j['title'] == title


def test_update_positive(session, base_url):
    """"Update first item"""
    userId = 1
    id = 1
    title = "Change number 1"
    payload = {'userId': userId, 'id': id, 'title': title}
    res = session.put(url=f'{base_url}/{userId}', json=payload)

    assert res.status_code == 200
    res_json = res.json()
    assert res_json['title'] == title


def test_update_negative():
    """"An attempt to update a non-existent item"""
    userId = -5
    id = 1
    url = 'https://jsonplaceholder.typicode.com/todos'
    payload = {'userId': userId, 'id': id, 1: 1}
    res = requests.put(f'{url}/{userId}', json=payload)
    assert res.status_code == 500


def test_delete(session, base_url):
    """"Delete item with id = 1"""
    id = 1
    res = session.delete(url=f'{base_url}/{id}')
    assert res.status_code == 200
    assert not res.json()


def test_filtering_resources(session, base_url):
    res = session.get(url=f'{base_url}?id={TODOS_MAX}')
    r = res.json()
    for f in r:
        assert f['userId'] == 10
        assert f['id'] == TODOS_MAX
        assert f['title'] == 'ipsam aperiam voluptates qui'
        assert f['completed'] == False


@pytest.mark.parametrize('items', ['id=201', 'title=i', 'userId=15', 'completed=Null'])
def test_filtering_resources_neg(session, base_url, items):
    res = session.get(url=f'{base_url}?{items}')
    assert res.status_code == 200
    r = res.json()
    for f in r:
        assert f['userId'] == []
        assert f['id'] == []
        assert f['title'] == []
        assert f['completed'] == []

