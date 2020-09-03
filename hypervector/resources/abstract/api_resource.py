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
    def list(cls):
        endpoint = hypervector.API_BASE + "/" + cls.resource_name + "/list"
        response = requests.get(endpoint, headers=cls.get_headers())
        return [cls.from_dict_for_lists(obj) for obj in response.json()]

    @classmethod
    def get(cls, uuid):
        endpoint = hypervector.API_BASE + "/" + cls.resource_name
        data = {cls.resource_name + "_uuid": uuid}
        response = requests.get(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_dict(response)

