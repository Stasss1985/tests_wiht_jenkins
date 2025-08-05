import requests


# from petstoreapiclient import PetStoreApiClient - это стало не нужным при модификации
# p = PetStoreApiClient # пока инициализируем его прямо здесь

# from urllib.parse import unquote
# Чтобы в консоли отображался текст без кодирования URL (т.е. в читаемом формате),
# вы можете использовать функцию urllib.parse.unquote. Эта функция декодирует URL,
# заменяя закодированные символы на их оригинальные значения.
# print(unquote(r.url)) # Декодируем URL

# Выполняем запрос
def test_get_pet_by_status(api_client):
    r = api_client.get_pet_by_status(params={'status': 'available'})
    json_response = r.json()
    print(json_response[2])
    assert r.status_code == 200
    assert len(json_response) > 1


def test_post_pet(api_client):
    body = {
        "id": 5654,
        "category": {
            "id": 2,
            "name": "dogs"
        },
        "name": "kolobok",
        "photoUrls": [
            "http://dkdk.img"
        ],
        "tags": [
            {
                "id": 32,
                "name": "string"
            }
        ],
        "status": "available"
    }
    r = api_client.create_pet(body=body)
    assert r.status_code == 200


def test_add_and_get_pet(api_client):
    body = {
        "id": 5654,
        "category": {
            "id": 155,
            "name": "dog"
        },
        "name": "doggie",
        "photoUrls": [
            "http://dkdk.img"
        ],
        "tags": [
            {
                "id": 25,
                "name": "string"
            }
        ],
        "status": "available"
    }
    r_create = api_client.create_pet(body=body)
    pet_name_create = r_create.json()['name']
    r_get = api_client.get_pet_by_status(params={'status': 'available'})
    json_response = r_get.json()
    pet_name_get = json_response[0]['name']
    print(json_response[2])
    print(pet_name_create, pet_name_get)
    assert pet_name_create == pet_name_get
    assert r_get.status_code == 200
    assert len(json_response) > 1


def test_post_pet_autoriz():
    body = {
        "id": 5654,
        "category": {
            "id": 2,
            "name": "dogs"
        },
        "name": "kolobok",
        "photoUrls": [
            "http://dkdk.img"
        ],
        "tags": [
            {
                "id": 32,
                "name": "string"
            }
        ],
        "status": "available"
    }
    headers = {"Autorization": "special-key"}  # для меня "Autorization": "Bearer accesstoken"
    r = requests.post('https://petstore.swagger.io/v2/pet',
                      json=body,
                      headers=headers)  # авторизация по accesstoken или "special-key"

    assert r.status_code == 200
