from random import random

import hypervector
from tests.util import get_resource_path


def test_benchmark():
    benchmarks = hypervector.Benchmark.list()
    assert isinstance(benchmarks[0], hypervector.Benchmark)


def test_benchmark_create():

    n_hypervectors = 10000

    new_project = hypervector.Project.new()
    new_definition = hypervector.Definition.new(project_uuid=new_project.project_uuid,
                                                definition_file=get_resource_path("hyperdef.json"))
    new_ensemble = hypervector.Ensemble.new(
        new_definition.definition_uuid,
        n_hypervectors
    )

    benchmark_results = [random() for _ in range(n_hypervectors)]

    benchmark = hypervector.Benchmark.new(
        new_ensemble.ensemble_uuid,
        benchmark_results
    )

    assert isinstance(benchmark, hypervector.Benchmark)
