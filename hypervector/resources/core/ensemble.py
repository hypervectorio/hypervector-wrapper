import requests

import hypervector
from hypervector.resources.abstract.api_resource import APIResource


class Ensemble(APIResource):
    resource_name = 'ensemble'

    def __init__(self, ensemble_uuid, N, benchmark_uuids):
        self.ensemble_uuid = ensemble_uuid
        self.N = N
        self.benchmark_uuids = benchmark_uuids

    @classmethod
    def from_dict(cls, ensemble_uuid, dictionary):
        return cls(
            ensemble_uuid=ensemble_uuid,
            N=dictionary['N'],
            benchmark_uuids=dictionary['benchmarks']
        )

    @classmethod
    def from_dict_for_lists(cls, dictionary):
        return cls(
            ensemble_uuid=dictionary['ensemble_uuid'],
            N=dictionary['n'],
            benchmark_uuids=None
        )

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            ensemble_uuid=dictionary['ensemble_uuid'],
            N=dictionary['n'],
            benchmark_uuids=None
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




