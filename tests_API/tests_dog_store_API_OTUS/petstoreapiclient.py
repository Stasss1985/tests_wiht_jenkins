import requests


class PetStoreApiClient:
    def __init__(self, base_url='https://petstore.swagger.io'):
        self.base_url = base_url
        self.session = requests.Session()

    def authorize(self, token='special-key'):
        # code for getting token
        self.session.headers['Authorization'] = token

    def get_pet_by_status(self, params=None):  # avalible, pending, sold
        r = self.session.get(f"{self.base_url}/v2/pet/findByStatus", params=params)
        return r

    def create_pet(self, body=None, params=None):  # avalible, pending, sold
        r = self.session.post(f"{self.base_url}/v2/pet", params=params, json=body) # передаем тело в виде json
        return r