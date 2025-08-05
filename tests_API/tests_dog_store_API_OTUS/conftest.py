from pytest import fixture
from petstoreapiclient import PetStoreApiClient


@fixture(scope="session")
def api_client():
    p = PetStoreApiClient(base_url="https://petstore.swagger.io")
    p.authorize()
    return p
