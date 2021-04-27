import requests
import hypervector
from hypervector.errors import APIKeyNotSetError, HypervectorError, APIConnectionError


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
    def request(cls, endpoint, method=requests.get, json=None):
        try:
            response = method(url=endpoint, headers=cls.get_headers(), json=json)
        except requests.ConnectionError:
            raise APIConnectionError(
                "There was a problem reaching the Hypervector API. Please "
                "check your hypervector.API_BASE setting"
            )

        if response.ok:
            return response.json()
        else:
            raise HypervectorError(response)

    @classmethod
    def get(cls, uuid):
        endpoint = f'{hypervector.API_BASE}/{cls.resource_name}/{uuid}'
        response = cls.request(endpoint)
        return cls.from_response(response)

    @classmethod
    def delete(cls, uuid):
        endpoint = f'{hypervector.API_BASE}/{cls.resource_name}/{uuid}/delete'
        response = requests.delete(endpoint, headers=cls.get_headers())
        return response

