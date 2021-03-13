import uuid

import pytest

import hypervector
from hypervector.errors import APIKeyNotSetError, HypervectorError
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


def test_no_api_key(monkeypatch):
    def mock_empty_api_key():
        return None

    monkeypatch.setattr(hypervector, 'API_KEY', mock_empty_api_key())

    with pytest.raises(APIKeyNotSetError):
        hypervector.Project.list()


def test_get_resource(test_definition, test_ensemble, test_benchmark):
    definition = hypervector.Definition.get(test_definition.definition_uuid)
    ensemble = hypervector.Ensemble.get(test_ensemble.ensemble_uuid)
    benchmark = hypervector.Benchmark.get(test_benchmark.benchmark_uuid)

    assert definition.definition_uuid == test_definition.definition_uuid
    assert ensemble.ensemble_uuid == test_ensemble.ensemble_uuid
    assert benchmark.benchmark_uuid == test_benchmark.benchmark_uuid


def test_get_resource_not_found():
    with pytest.raises(HypervectorError) as error:
        hypervector.Definition.get(str(uuid.uuid4()))
        assert error.status_code == 404


def test_delete_resource(test_definition, test_ensemble, test_benchmark):
    hypervector.Benchmark.delete(test_benchmark.benchmark_uuid)
    with pytest.raises(HypervectorError) as error:
        hypervector.Benchmark.get(test_benchmark.benchmark_uuid)
        assert error.status_code == 404

    hypervector.Ensemble.delete(test_ensemble.ensemble_uuid)
    with pytest.raises(HypervectorError) as error:
        hypervector.Ensemble.get(test_ensemble.ensemble_uuid)
        assert error.status_code == 404

    hypervector.Definition.delete(test_definition.definition_uuid)
    with pytest.raises(HypervectorError):
        hypervector.Definition.get(test_definition.definition_uuid)
        assert error.status_code == 404






