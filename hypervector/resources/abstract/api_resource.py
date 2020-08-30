import requests
import hypervector


class APIResource:

    @classmethod
    def list(cls):

        HEADERS = {
            'content-type': 'application/json',
            'x-api-key': hypervector.API_KEY
        }

        response = requests.get(hypervector.API_BASE + "/project/list", headers=HEADERS)
        return response.json()

