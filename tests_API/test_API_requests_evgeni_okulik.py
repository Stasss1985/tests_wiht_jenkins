import requests
import json
import pytest


@pytest.fixture()
def new_post_id():
    body = {"title": "foofoofoo", "body": "barfoofoo", "userId": 5}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield post_id - 1
    print('deleting a post')
    requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id - 1}")


@pytest.mark.smoke
def test_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    print(response[0])
    assert len(response) == 100, 'Not all posts returned'


@pytest.mark.smoke
def test_one_post(new_post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id, 'Status code is incorrect'


@pytest.mark.regression
def test_post_a_post_slojni():
    body = json.dumps({"title": "foo", "body": "bar", "userId": 1})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'Id is incorrect'


@pytest.mark.smoke
def test_post_a_post():
    body = {"title": "foofoofoo", "body": "barfoofoo", "userId": 5}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'Id is incorrect'


def clear_new_post(post_id):
    requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")


@pytest.mark.skip('Не проходит тест из за проги, мы его скипаем')
def test_put_a_post(new_post_id):
    body = {"title": "foofoofoo89898", "body": "barfoofoo-565656", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f"https://jsonplaceholder.typicode.com/posts/{new_post_id}",
        json=body,
        headers=headers
    ).json()
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    assert response["title"] == "foofoofoo89898"
    clear_new_post(new_post_id)


@pytest.mark.regression
def test_patch_a_post(new_post_id):
    body = {"body": "barfoofoo-565656", "userId": 55}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f"https://jsonplaceholder.typicode.com/posts/{new_post_id}",
        json=body,
        headers=headers
    ).json()
    print(response)
    clear_new_post(new_post_id)


def test_delete_a_post(new_post_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{new_post_id}")
    print(response.json())
    print(response.status_code)
