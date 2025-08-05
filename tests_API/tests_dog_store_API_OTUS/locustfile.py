from locust import task, HttpUser
from petstoreapiclient import PetStoreApiClient
import pytest
import requests


# base_url = 'https://petstore.swagger.io'

class PetPerformance(HttpUser):
    # host = "https://petstore.swagger.io"  # Обязательное поле!
    host = "https://erp-test.karman24.ru"

    # token = None
    @task
    def get_all_list(self):
        token = (
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiN2FhYWQ0ZjAwY2QxN2NkZTNlMTM1ZGExZTRmOGExOTQzYzQ5MmQ4ZjNlMTg0Mjk3N2M0"
            "MzczZGUyZjAxODFhMTBiYTQ0NmM5NzA1ZjZlNDMiLCJpYXQiOjE3NTEyMjI3NjguMTY0NDM0LCJuYmYiOjE3NTEyMjI3NjguMTY0NDM3LCJleHAiOjE3NTEyMzA4MDAu"
            "MTUwMTM0LCJzdWIiOiIzMzMiLCJzY29wZXMiOlsiKiJdfQ.ZwZaYsq4hzo8kPi-TH9rpSrV3aPkVOBfBh299ClQ44CAf_Dmz_Nnt_rRU39A4TmrNNPHL-a8xnO3cWfob"
            "VQbJ2igYdWyEm143q7JhGdMqRQEKkpPVbPsFh17XmNgEWG1wInzUGfaRfykd3NOBwA90vSt53tpBBC6Nm9asrtE9fZoO20KCu5ri_Y1zPTKIn6rb07xx9iRu-OzaQ"
            "aVZqR1VEY5-dMOI4fjIrsIFNSUiemj5Dp0goolvFCIXQecQCf3aJtFtlm_UVQ1BuUaUZIugJhuP2sl-YhdUapZynwOlxsMIermTAAWrxnz1ZjowU-WOtkJpCF8jcQ"
            "XmKjlb7e_LZ53hqS99LzLw4O2qDRVlI9jA6B9NP0FEL84v7OeiLWRwnY5a1uYx6F_CR_octAhI4CnrvvZB1sDu6EiNsPYN8NjbbnbXqT61gtnF4ZohXo0kc7W57O"
            "PI-zC856qLVr-20GHP58i9sOTjOQ4yoqi-ofpfjVVXmbtWfNMYhu7OYvN9vVHyLf15bRXxe5rwfIEo1afBAKHkh-u3fLVz22v7ycy-qnCO-UZtCBCHiVg0jAcjDt8"
            "C7RPSyn5KzJu890FF6WVnJhZVR3XXVhxzhnhZoX_L1WcekgAfniriAaIXpbaO2QqZok6ay4kQoszgtFZN14zCJyxZaYcra7XPD5Sf2U"
        )
        try:
            response = self.client.get('/user/all-list', headers={'Authorization': f'Bearer {token}'})
            # Добавьте проверку ответа
            if response.status_code != 200:
                print(f"Error! Status: {response.status_code}, Response: {response.text}")
                return
            if response.status_code == 200:
                print(f"Status: {response.status_code}, Response: {response.text}")
                return

            # Обработка успешного ответа
            print("Request successful!")

        except Exception as e:
            print(f"Request failed: {str(e)}")

    @task
    def get_person_10000(self):
        token = (
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiN2FhYWQ0ZjAwY2QxN2NkZTNlMTM1ZGExZTRmOGExOTQzYzQ5MmQ4ZjNlMTg0Mjk3N2M0"
            "MzczZGUyZjAxODFhMTBiYTQ0NmM5NzA1ZjZlNDMiLCJpYXQiOjE3NTEyMjI3NjguMTY0NDM0LCJuYmYiOjE3NTEyMjI3NjguMTY0NDM3LCJleHAiOjE3NTEyMzA4MDAu"
            "MTUwMTM0LCJzdWIiOiIzMzMiLCJzY29wZXMiOlsiKiJdfQ.ZwZaYsq4hzo8kPi-TH9rpSrV3aPkVOBfBh299ClQ44CAf_Dmz_Nnt_rRU39A4TmrNNPHL-a8xnO3cWfob"
            "VQbJ2igYdWyEm143q7JhGdMqRQEKkpPVbPsFh17XmNgEWG1wInzUGfaRfykd3NOBwA90vSt53tpBBC6Nm9asrtE9fZoO20KCu5ri_Y1zPTKIn6rb07xx9iRu-OzaQ"
            "aVZqR1VEY5-dMOI4fjIrsIFNSUiemj5Dp0goolvFCIXQecQCf3aJtFtlm_UVQ1BuUaUZIugJhuP2sl-YhdUapZynwOlxsMIermTAAWrxnz1ZjowU-WOtkJpCF8jcQ"
            "XmKjlb7e_LZ53hqS99LzLw4O2qDRVlI9jA6B9NP0FEL84v7OeiLWRwnY5a1uYx6F_CR_octAhI4CnrvvZB1sDu6EiNsPYN8NjbbnbXqT61gtnF4ZohXo0kc7W57O"
            "PI-zC856qLVr-20GHP58i9sOTjOQ4yoqi-ofpfjVVXmbtWfNMYhu7OYvN9vVHyLf15bRXxe5rwfIEo1afBAKHkh-u3fLVz22v7ycy-qnCO-UZtCBCHiVg0jAcjDt8"
            "C7RPSyn5KzJu890FF6WVnJhZVR3XXVhxzhnhZoX_L1WcekgAfniriAaIXpbaO2QqZok6ay4kQoszgtFZN14zCJyxZaYcra7XPD5Sf2U"
        )
        try:
            response = self.client.get('/person/10000', headers={'Authorization': f'Bearer {token}'})
            # Добавьте проверку ответа
            if response.status_code != 200:
                print(f"Error! Status: {response.status_code}, Response: {response.text}")
                return
            if response.status_code == 200:
                print(f"Status: {response.status_code}, Response: {response.text}")
                return

            # Обработка успешного ответа
            print("Request successful!")

        except Exception as e:
            print(f"Request failed: {str(e)}")

# def on_start(self):
#     response = self.client.post('/auth', json={'email': '...', 'password': '...'})
#     print(f"Status Code: {response.status_code}")  # Добавьте это
#     print(f"Response Text: {response.text}")  # И это
#     self.token = response.json()['token']


# @task
# def get_pet_by_status_performance(self):
#     self.client.get(f"/v2/pet/findByStatus", params={'status': 'available'})

# @task
# def erp_test_karman24(self):
#     self.client.get(f"/auth")
