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


