import requests
import hypervector


def get_api_key():
    from hypervector import API_KEY
    return API_KEY


class APIResource:
    headers = {'content-type': 'application/json'}

    @classmethod
    def get_headers(cls):
        cls.headers['x-api-key'] = get_api_key()
        return cls.headers

    @classmethod
    def get(cls, uuid):
        endpoint = f'{hypervector.API_BASE}/{cls.resource_name}/{uuid}'
        response = requests.get(endpoint, headers=cls.get_headers())
        if response.status_code == 200:
            return cls.from_response_get(response.json())
        else:
            return None

    @classmethod
    def delete(cls, uuid):
        endpoint = f'{hypervector.API_BASE}/{cls.resource_name}/{uuid}/delete'
        response = requests.delete(endpoint, headers=cls.get_headers()).json()
        return response

