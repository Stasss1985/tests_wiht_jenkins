import requests


# from urllib.parse import unquote
# Чтобы в консоли отображался текст без кодирования URL (т.е. в читаемом формате),
# вы можете использовать функцию urllib.parse.unquote. Эта функция декодирует URL,
# заменяя закодированные символы на их оригинальные значения.
# print(unquote(r.url)) # Декодируем URL

# Выполняем запрос
def test_get_pet_by_status():
    r = requests.get('https://petstore.swagger.io/v2/pet/findByStatus',
                     params={'status': 'available'})
    json_response = r.json()
    print(json_response[2])
    assert r.status_code == 200
    assert len(json_response) > 1


def test_post_pet():
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
    r = requests.post('https://petstore.swagger.io/v2/pet',
                      json=body,
                      auth=('login', 'password'))  # авторизация по логину и паролю

    assert r.status_code == 200


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


def test_post_autoriz():
    body = {
        "id": 5654,
        
        }
    headers = {"Autorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZDEzMGIxZDE2N2Y1NWFhMWM3Zjk4ZDE2ZDk5YWYwY2IyOGY1MmU1N2IxZTU1MDIwMTRjOGQyYmJmNDdjN2IxNzAwYjIyMmQzYjllMDdkMDgiLCJpYXQiOjE3NDI5ODg0ODIuODAxOTU3LCJuYmYiOjE3NDI5ODg0ODIuODAxOTU5LCJleHAiOjE3NzQ1MjQ0ODIuNzk2NDgyLCJzdWIiOiIzMzMiLCJzY29wZXMiOlsiKiJdfQ.agPRdgjw - wVWx8dAaxppZKTgGQUCESI5qJgU90hCW7qDQ3uZ52NSzBz94WynDZcelGK2kHd2ssKdTSsNjJm2HX5bR6KcfIqm9kH9rSKJKIMyY - gAMvs0l4mib - 9 kOEuxI9akQ4XfdDYHCustTUEStyyw - oFNbMaJefMU7bT8QSmpsrOsSGV66iXG8cPGSfklExBuaEhVIz2Inp4IBhLstY08H6MVND9LemR5PKKrKO - M7_QVEkkG1yfGVXjzcggsPDtg2hZtac52Bj5OP8o4 - HSIF2 - N9Jj3pgZDGUKsKwkG - 7 gxJROq8x00w6FrYzHghIB - mudJFQAE1TTdfJqwCnpnllQErni2cI9JMJ41Mj4qKpuOYixcjvmfHQ720pI_jRreXq4bC9qyVBaK4XCmpmEvF7xAo7dhPOs2WW29dYyd2qFzdFaQp7LOK - tPxuRGtNqU - CtVQTJFBk0YKuY1FJskIYFA7qcXK5BSfw2OH - EDwk8ALbOlpOvCvEenegBht_d_R1RoavndzU0cJxhLjVHWTKSsYSGuwy7kftSHAiuvDH01Xs5ddaTxqU5r13GF9Q10pr3zuSmtfE9gfhWxoteoyUeScf0qHq6IFcCvM6BsDl99OY6uYiX5vdBuDsGNUD7233hPm7_z - nK6z6BrDFU1le81WvO6TBacJvY90xo"}
    r = requests.post('https://erp-api-test.karman24.ru/oauth/token',
                      json=body,
                      headers=headers)  # авторизация по accesstoken или "special-key"

    assert r.status_code == 200


