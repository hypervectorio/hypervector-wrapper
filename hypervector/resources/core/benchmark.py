import requests

import hypervector
from hypervector.resources.abstract.api_resource import APIResource


class Benchmark(APIResource):
    resource_name = 'benchmark'

    def __init__(self, benchmark_uuid, ensemble_uuid):
        self.benchmark_uuid = benchmark_uuid
        self.ensemble_uuid = ensemble_uuid

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            benchmark_uuid=dictionary['benchmark_uuid'],
            ensemble_uuid=dictionary['ensemble_uuid']
        )

    @classmethod
    def from_response_get(cls, dictionary):
        return cls.from_response(dictionary)

    @classmethod
    def list(cls, ensemble_uuid):
        endpoint = f"{hypervector.API_BASE}/ensemble/{ensemble_uuid}/benchmark/list"
        response = requests.get(endpoint, headers=cls.get_headers())
        return [cls.from_response(obj) for obj in response.json()]

    @classmethod
    def new(cls, ensemble_uuid, output):
        endpoint = f"{hypervector.API_BASE}/ensemble/{ensemble_uuid}/benchmark/add"
        data = {"output": output}
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)

    def assert_equal(self, output):
        endpoint = f"{hypervector.API_BASE}/ensemble/{self.ensemble_uuid}/{self.resource_name}/{self.benchmark_uuid}/assert"
        data = {"output": output}
        response = requests.post(endpoint, json=data, headers=self.get_headers()).json()
        return response
