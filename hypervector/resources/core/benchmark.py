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