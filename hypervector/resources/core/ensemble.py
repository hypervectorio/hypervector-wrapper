import requests

import hypervector
from hypervector.resources.abstract.api_resource import APIResource
from hypervector.resources.core.benchmark import Benchmark


class Ensemble(APIResource):
    resource_name = 'ensemble'

    def __init__(self, ensemble_uuid, N, benchmarks):
        self.ensemble_uuid = ensemble_uuid
        self.N = N
        self.benchmarks = benchmarks

    @classmethod
    def from_dict(cls, ensemble_uuid, dictionary):
        return cls(
            ensemble_uuid=ensemble_uuid,
            N=dictionary['N'],
            benchmarks=_parse_benchmarks(dictionary['benchmarks'])
        )

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            ensemble_uuid=dictionary['ensemble_uuid'],
            N=dictionary['n'],
            benchmarks=None
        )

    @classmethod
    def from_response_get(cls, dictionary):
        # Return hypervectors on get
        ensemble_result = EnsembleResult(
            ensemble_uuid=dictionary['ensemble_uuid'],
            hypervectors=dictionary['hypervectors']
        )

        return ensemble_result

    @classmethod
    def new(cls, definition_uuid, N):
        endpoint = f"{hypervector.API_BASE}/{cls.resource_name}"
        data = {"definition_uuid": definition_uuid, "N": N}
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)


class EnsembleResult:

    def __init__(self, ensemble_uuid, hypervectors):
        self.ensemble_uuid = ensemble_uuid
        self.hypervectors = hypervectors


def _parse_benchmarks(benchmarks):
    parsed_benchmarks = []
    for benchmark_uuid in benchmarks:
        parsed_benchmark = Benchmark(benchmark_uuid=benchmark_uuid)
        parsed_benchmarks.append(parsed_benchmark)
    return parsed_benchmarks




