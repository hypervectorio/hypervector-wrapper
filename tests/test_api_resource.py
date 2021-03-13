import pytest
import hypervector
from tests.util import get_resource_path


@pytest.fixture
def test_definition():
    project = hypervector.Project.new()
    definition = hypervector.Definition.new(
        definition_file=get_resource_path("hyperdef.json"),
        project_uuid=project.project_uuid
    )
    return definition


@pytest.fixture
def test_ensemble(test_definition):
    ensemble = hypervector.Ensemble.new(
        definition_uuid=test_definition.definition_uuid,
        size=100
    )
    return ensemble


@pytest.fixture
def test_benchmark(test_ensemble):
    benchmark = hypervector.Benchmark.new(
        ensemble=test_ensemble,
        expected_output=[1 for _ in range(test_ensemble.size)]
    )
    return benchmark


def test_get_resource():
    projects = hypervector.Project.list()

    assert len(projects) > 0

    for project in projects:
        assert isinstance(project, hypervector.Project)

        if project.definitions:
            for definition_meta in project.definitions:
                definition = hypervector.Definition.get(definition_meta.definition_uuid)
                assert isinstance(definition, hypervector.Definition)


def test_delete_resource(test_definition, test_ensemble, test_benchmark):
    hypervector.Benchmark.delete(test_benchmark.benchmark_uuid)
    assert hypervector.Benchmark.get(test_benchmark.benchmark_uuid) is None

    hypervector.Ensemble.delete(test_ensemble.ensemble_uuid)
    assert hypervector.Ensemble.get(test_ensemble.ensemble_uuid) is None

    hypervector.Definition.delete(test_definition.definition_uuid)
    assert hypervector.Definition.get(test_definition.definition_uuid) is None






