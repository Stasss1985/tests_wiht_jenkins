import pytest
import requests


def test_on_start():
    response = requests.post('https://erp-test.karman24.ru/auth',
                             json={'email': '', 'password': ''})
    print(f"Status Code: {response.status_code}")  # Добавьте это
    #     print(f"Response Text: {response.text}")  # И это
    #     self.token = response.json()['token']


def get_support_ticket():
    # Конфигурация теста
    base_url = "https://erp-api-test.karman24.ru"  # Замените на ваш базовый URL
    endpoint = "/support/ticket"

    # Токен авторизации
    token = (
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiN2FhYWQ0ZjAwY2QxN2NkZTNlMTM1ZGExZTRmOGExOTQzYzQ5MmQ4ZjNlMTg0Mjk3N2M0"
        "MzczZGUyZjAxODFhMTBiYTQ0NmM5NzA1ZjZlNDMiLCJpYXQiOjE3NTEyMjI3NjguMTY0NDM0LCJuYmYiOjE3NTEyMjI3NjguMTY0NDM7LCJleHAiOjE3NTEyMzA4MDAu"
        "MTUwMTM0LCJzdWIiOiIzMzMiLCJzY29wZXMiOlsiKiJdfQ.ZwZaYsq4hzo8kPi-TH9rpSrV3aPkVOBfBh299ClQ44CAf_Dmz_Nnt_rRU39A4TmrNNPHL-a8xnO3cWfob"
        "VQbJ2igYdWyEm143q7JhGdMqRQEKkpPVbPsFh17XmNgEWG1wInzUGfaRfykd3NOBwA90vSt53tpBBC6Nm9asrtE9fZoO20KCu5ri_Y1zPTKIn6rb07xx9iRu-OzaQ"
        "aVZqR1VEY5-dMOI4fjIrsIFNSUiemj5Dp0goolvFCIXQecQCf3aJtFtlm_UVQ1BuUaUZIugJhuP2sl-YhdUapZynwOlxsMIermTAAWrxnz1ZjowU-WOtkJpCF8jcQ"
        "XmKjlb7e_LZ53hqS99LzLw4O2qDRVlI9jA6B9NP0FEL84v7OeiLWRwnY5a1uYx6F_CR_octAhI4CnrvvZB1sDu6EiNsPYN8NjbbnbXqT61gtnF4ZohXo0kc7W57O"
        "PI-zC856qLVr-20GHP58i9sOTjOQ4yoqi-ofpfjVVXmbtWfNMYhu7OYvN9vVHyLf15bRXxe5rwfIEo1afBAKHkh-u3fLVz22v7ycy-qnCO-UZtCBCHiVg0jAcjDt8"
        "C7RPSyn5KzJu890FF6WVnJhZVR3XXVhxzhnhZoX_L1WcekgAfniriAaIXpbaO2QqZok6ay4kQoszgtFZN14zCJyxZaYcra7XPD5Sf2U"
    )

    # Формируем заголовки
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        # Отправляем GET-запрос
        response = requests.get(
            f"{base_url}{endpoint}",
            headers=headers,
        )

        # Выводим информацию для отладки
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:100]}...")  # Выводим первые 500 символов

        # Проверяем статус код
        assert response.status_code == 200, (
            f"Ожидался статус 200, получен {response.status_code}"
        )

        # Проверяем, что ответ в формате JSON
        response_data = response.json()
        assert isinstance(response_data, (list, dict)), "Ответ должен быть JSON-объектом"
        print("Тест успешно пройден!")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Ошибка сети: {str(e)}")
    except ValueError as e:
        pytest.fail(f"Ошибка парсинга JSON: {str(e)}")
