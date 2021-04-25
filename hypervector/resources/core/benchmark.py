import numpy as np
import requests

import hypervector
from hypervector.resources.abstract.api_resource import APIResource


class Benchmark(APIResource):
    resource_name = 'benchmark'

    def __init__(self, benchmark_uuid, ensemble_uuid, definition_uuid):
        self.benchmark_uuid = benchmark_uuid
        self.ensemble_uuid = ensemble_uuid
        self.definition_uuid = definition_uuid

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            benchmark_uuid=dictionary['benchmark_uuid'],
            ensemble_uuid=dictionary['ensemble_uuid'],
            definition_uuid=dictionary['definition_uuid']
        )

    def to_response(self):
        return {
            "benchmark_uuid": self.benchmark_uuid,
            "ensemble_uuid": self.ensemble_uuid,
            "definition_uuid": self.definition_uuid
        }

    @classmethod
    def from_get(cls, response):
        return cls.from_response(response.json())

    def refresh(self):
        benchmark = self.get(self.benchmark_uuid)
        self.__dict__.update(benchmark.__dict__)

    @classmethod
    def list(cls, ensemble):
        parent_endpoint = f"{hypervector.API_BASE}/definition/{ensemble.definition_uuid}" \
                          f"/ensemble/{ensemble.ensemble_uuid}"
        endpoint = f"{parent_endpoint}/benchmarks"
        response = cls.request(endpoint)
        return [cls.from_response(obj) for obj in response]

    @classmethod
    def new(cls, ensemble, expected_output):
        endpoint = f"{hypervector.API_BASE}/definition/{ensemble.definition_uuid}" \
                   f"/ensemble/{ensemble.ensemble_uuid}/benchmarks/add"

        if isinstance(expected_output, np.ndarray):
            expected_output = expected_output.tolist()

        data = {"expected_output": expected_output}
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)

    def assert_equal(self, output_to_assert):
        endpoint = f"{hypervector.API_BASE}/benchmark/{self.benchmark_uuid}/assert"

        if isinstance(output_to_assert, np.ndarray):
            output_to_assert = output_to_assert.tolist()

        data = {"output_to_assert": output_to_assert}
        response = requests.post(endpoint, json=data, headers=self.get_headers()).json()
        return response
