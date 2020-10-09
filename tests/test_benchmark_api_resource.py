from random import random
import pytest
import hypervector
from tests.util import get_resource_path


@pytest.fixture
def ensemble_for_test():
    n_hypervectors = 10000
    new_project = hypervector.Project.new()
    new_definition = hypervector.Definition.new(project_uuid=new_project.project_uuid,
                                                definition_file=get_resource_path("hyperdef.json"))
    new_ensemble = hypervector.Ensemble.new(
        new_definition.definition_uuid,
        n_hypervectors
    )

    return new_ensemble, n_hypervectors


def test_benchmark_list():
    benchmarks = hypervector.Benchmark.list()

    for benchmark in benchmarks:
        assert isinstance(benchmark, hypervector.Benchmark)


def test_benchmark_new(ensemble_for_test):
    new_ensemble, n_hypervectors = ensemble_for_test

    benchmark_results = [random() for _ in range(n_hypervectors)]

    benchmark = hypervector.Benchmark.new(
        new_ensemble.ensemble_uuid,
        benchmark_results
    )

    assert isinstance(benchmark, hypervector.Benchmark)


def test_benchmark_assert(ensemble_for_test):
    new_ensemble, n_hypervectors = ensemble_for_test

    benchmark_results = [random() for _ in range(n_hypervectors)]
    failing_results = [random() for _ in range(n_hypervectors)]

    benchmark = hypervector.Benchmark.new(
        new_ensemble.ensemble_uuid,
        benchmark_results
    )

    assert benchmark.compare(benchmark_results) == {'result': 'PASSED'}
    assert benchmark.compare(failing_results) == {'result': 'FAILED'}
    

