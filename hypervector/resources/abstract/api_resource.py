import requests
import hypervector


class APIResource:

    @classmethod
    def list(cls):
        headers = {
            'content-type': 'application/json',
            'x-api-key': hypervector.API_KEY
        }
        endpoint = hypervector.API_BASE + "/" + cls.resource_name + "/list"
        response = requests.get(endpoint, headers=headers)

        return [cls.from_dict_for_lists(obj) for obj in response.json()]

    @classmethod
    def get(cls, uuid):
        headers = {
            'content-type': 'application/json',
            'x-api-key': hypervector.API_KEY
        }
        endpoint = hypervector.API_BASE + "/" + cls.resource_name
        data = {cls.resource_name + "_uuid": uuid}
        response = requests.get(endpoint, json=data, headers=headers).json()

        return cls.from_dict(response)

