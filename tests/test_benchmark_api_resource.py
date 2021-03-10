from random import random
import pytest
import hypervector
from tests.util import get_resource_path


@pytest.fixture
def ensemble_for_test():
    new_project = hypervector.Project.new()
    new_definition = hypervector.Definition.new(project_uuid=new_project.project_uuid,
                                                definition_file=get_resource_path("hyperdef.json"))
    new_ensemble = hypervector.Ensemble.new(
        definition_uuid=new_definition.definition_uuid,
        size='MEDIUM'
    )

    return new_ensemble


def test_benchmark_list(ensemble_for_test):
    benchmarks = hypervector.Benchmark.list(ensemble_for_test)

    for benchmark in benchmarks:
        assert isinstance(benchmark, hypervector.Benchmark)


def test_benchmark_new(ensemble_for_test):
    benchmark_results = [random() for _ in range(ensemble_for_test.size)]

    benchmark = hypervector.Benchmark.new(
        ensemble=ensemble_for_test,
        expected_output=benchmark_results
    )

    assert isinstance(benchmark, hypervector.Benchmark)


def test_benchmark_assert(ensemble_for_test):
    benchmark_results = [random() for _ in range(ensemble_for_test.size)]
    failing_results = [random() for _ in range(ensemble_for_test.size)]

    benchmark = hypervector.Benchmark.new(
        ensemble=ensemble_for_test,
        expected_output=benchmark_results
    )

    assert benchmark.assert_equal(benchmark_results)['asserted'] is True
    assert benchmark.assert_equal(failing_results)['asserted'] is False
    

