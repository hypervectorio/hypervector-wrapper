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
    def new(cls, ensemble_uuid, output_hash):
        endpoint = f"{hypervector.API_BASE}/{cls.resource_name}"
        data = {'ensemble_uuid': ensemble_uuid, "output_hash": output_hash}
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)