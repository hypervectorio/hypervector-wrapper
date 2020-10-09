import requests

import hypervector
from hypervector.resources.abstract.api_resource import APIResource


class Benchmark(APIResource):
    resource_name = 'benchmark'

    def __init__(self, benchmark_uuid):
        self.benchmark_uuid = benchmark_uuid

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            benchmark_uuid=dictionary['benchmark_uuid']
        )

    @classmethod
    def from_response_get(cls, dictionary):
        return cls.from_response(dictionary)

    @classmethod
    def new(cls, ensemble_uuid, output):
        endpoint = f"{hypervector.API_BASE}/{cls.resource_name}"
        data = {'ensemble_uuid': ensemble_uuid, "output_hash": hash(tuple(output))}
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)

    def compare(self, output):
        endpoint = f"{hypervector.API_BASE}/{self.resource_name}/assert"
        data = {'benchmark_uuid': self.benchmark_uuid, "output_hash": hash(tuple(output))}
        response = requests.post(endpoint, json=data, headers=self.get_headers()).json()
        return response
