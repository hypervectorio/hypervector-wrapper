import requests
import hypervector
from hypervector.errors import APIKeyNotSetError, HypervectorError, APIBaseError


class APIResource:
    headers = {'content-type': 'application/json'}

    @classmethod
    def get_headers(cls):
        from hypervector import API_KEY

        if not API_KEY:
            raise APIKeyNotSetError

        cls.headers['x-api-key'] = API_KEY
        return cls.headers

    @classmethod
    def get(cls, uuid):
        endpoint = f'{hypervector.API_BASE}/{cls.resource_name}/{uuid}'
        try:
            response = requests.get(endpoint, headers=cls.get_headers())
        except requests.ConnectionError:
            raise APIBaseError

        if response.ok:
            return cls.from_get(response)
        else:
            raise HypervectorError

    @classmethod
    def request(cls, endpoint, method=requests.get):
        try:
            response = method(url=endpoint, headers=cls.get_headers())
        except requests.ConnectionError:
            raise APIBaseError

        if response.ok:
            return response.json()
        else:
            raise HypervectorError(response)

    @classmethod
    def delete(cls, uuid):
        endpoint = f'{hypervector.API_BASE}/{cls.resource_name}/{uuid}/delete'
        response = requests.delete(endpoint, headers=cls.get_headers())
        return response

