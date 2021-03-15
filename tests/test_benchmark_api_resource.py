import uuid
from random import random
import responses

import hypervector


def test_benchmark_list(mocked_resources, mocked_responses):
    _, definition, ensemble, benchmark = mocked_resources

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}/'
        f'ensemble/{ensemble.ensemble_uuid}/benchmarks',
        json=[
            benchmark.to_response(),
            benchmark.to_response(),
            benchmark.to_response()
        ]
    )

    retrieved_benchmarks = hypervector.Benchmark.list(ensemble)

    for retrieved_benchmark in retrieved_benchmarks:
        assert isinstance(retrieved_benchmark, hypervector.Benchmark)


def test_benchmark_new(mocked_resources):
    _, definition, ensemble, _ = mocked_resources
    benchmark_results = [random() for _ in range(ensemble.size)]

    benchmark = hypervector.Benchmark.new(
        ensemble=ensemble,
        expected_output=benchmark_results
    )

    assert isinstance(benchmark, hypervector.Benchmark)


def test_benchmark_assert(mocked_resources, mocked_responses):
    _, _, ensemble, benchmark = mocked_resources

    benchmark_results = [random() for _ in range(ensemble.size)]
    failing_results = [random() for _ in range(ensemble.size)]

    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/benchmark/{benchmark.benchmark_uuid}/assert',
        json={
            "assertion_uuid": str(uuid.uuid4()),
            "timestamp": "Mon, 1 Jan 1970 00:00:05 GMT",
            "benchmark_uuid": benchmark.benchmark_uuid,
            "ensemble_uuid": ensemble.ensemble_uuid,
            "asserted": True,
            "diff": None
        }
    )

    mocked_responses.add(
        responses.POST,
        f'{hypervector.API_BASE}/benchmark/{benchmark.benchmark_uuid}/assert',
        json={
            "assertion_uuid": str(uuid.uuid4()),
            "timestamp": "Mon, 1 Jan 1970 00:00:05 GMT",
            "benchmark_uuid": benchmark.benchmark_uuid,
            "ensemble_uuid": ensemble.ensemble_uuid,
            "asserted": False,
            "diff": None
        }
    )

    assert benchmark.assert_equal(benchmark_results)['asserted'] is True
    assert benchmark.assert_equal(failing_results)['asserted'] is False
    

