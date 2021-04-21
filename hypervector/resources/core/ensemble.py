import gzip
import json

import requests

import hypervector
from hypervector.resources.abstract.api_resource import APIResource
from hypervector.resources.core.benchmark import Benchmark


class Ensemble(APIResource):
    resource_name = 'ensemble'

    def __init__(self, ensemble_uuid, definition_uuid, size, benchmarks):
        self.ensemble_uuid = ensemble_uuid
        self.definition_uuid = definition_uuid
        self.size = size
        self.benchmarks = benchmarks

    @classmethod
    def from_dict(cls, ensemble_uuid, dictionary):
        return cls(
            ensemble_uuid=ensemble_uuid,
            size=dictionary['size'],
            benchmarks=_parse_benchmarks(dictionary['benchmarks'])
        )

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            ensemble_uuid=dictionary['ensemble_uuid'],
            definition_uuid=dictionary['definition_uuid'],
            size=dictionary['size'],
            benchmarks=_parse_benchmarks(dictionary['benchmarks'])
        )

    def to_response(self):
        return {
            "ensemble_uuid": self.ensemble_uuid,
            "definition_uuid": self.definition_uuid,
            "size": self.size,
            "benchmarks": self.benchmarks
        }

    @classmethod
    def from_get(cls, response):
        return cls.from_response(response.json())

    def refresh(self):
        ensemble = self.get(self.ensemble_uuid)
        self.__dict__.update(ensemble.__dict__)

    @classmethod
    def list(cls, definition):
        parent_endpoint = f"{hypervector.API_BASE}/definition/{definition.definition_uuid}"
        endpoint = f"{parent_endpoint}/ensembles"
        response = cls.request(endpoint)
        return [cls.from_response(ensemble) for ensemble in response]

    @classmethod
    def new(cls, definition_uuid, size):
        endpoint = f"{hypervector.API_BASE}/definition/{definition_uuid}/ensembles/add"
        data = {"size": size}
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)

    def hypervectors(self):
        endpoint = f"{hypervector.API_BASE}/ensemble/{self.ensemble_uuid}/data"
        response = requests.get(endpoint, headers=self.get_headers()).json()
        return response['hypervectors']


class EnsembleResult:

    def __init__(self, ensemble_uuid, hypervectors, size, benchmarks):
        self.ensemble_uuid = ensemble_uuid
        self.hypervectors = hypervectors
        self.size = size
        self.benchmarks = _parse_benchmarks(benchmarks)


def _parse_benchmarks(benchmarks):
    if not benchmarks or len(benchmarks) == 0:
        return None

    parsed_benchmarks = []
    for benchmark in benchmarks:
        parsed_benchmark = Benchmark(
            benchmark_uuid=benchmark['benchmark_uuid'],
            ensemble_uuid=benchmark['ensemble_uuid'],
            definition_uuid=benchmark['definition_uuid']
        )
        parsed_benchmarks.append(parsed_benchmark)
    return parsed_benchmarks




