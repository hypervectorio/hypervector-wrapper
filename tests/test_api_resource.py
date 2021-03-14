import uuid
import pytest
import requests
import responses

import hypervector
from hypervector.errors import APIKeyNotSetError, HypervectorError
from tests.util import get_resource_path


@pytest.fixture
def definition():
    project = hypervector.Project.new()
    definition = hypervector.Definition.new(
        definition_file=get_resource_path("hyperdef.json"),
        project_uuid=project.project_uuid
    )
    return definition


@pytest.fixture
def ensemble(definition):
    ensemble = hypervector.Ensemble.new(
        definition_uuid=definition.definition_uuid,
        size=100
    )
    return ensemble


@pytest.fixture
def benchmark(ensemble):
    benchmark = hypervector.Benchmark.new(
        ensemble=ensemble,
        expected_output=[1 for _ in range(ensemble.size)]
    )
    return benchmark


def test_no_api_key(monkeypatch):
    def mock_empty_api_key():
        return None

    monkeypatch.setattr(hypervector, 'API_KEY', mock_empty_api_key())

    with pytest.raises(APIKeyNotSetError):
        hypervector.Project.list()


@responses.activate
def test_get_resource(definition, ensemble, benchmark):
    responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}',
        json=definition.to_response()
    )

    retrieved_definition = hypervector.Definition.get(definition.definition_uuid)

    assert retrieved_definition.definition_uuid == definition.definition_uuid


@responses.activate
def test_get_resource_not_found():
    random_resource_uuid = str(uuid.uuid4())

    responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{random_resource_uuid}',
        status=404
    )

    with pytest.raises(HypervectorError) as error:
        hypervector.Definition.get(random_resource_uuid)
        assert error.status_code == 404


@responses.activate
def test_delete_resource(definition, ensemble, benchmark):
    endpoints = [
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}',
        f'{hypervector.API_BASE}/ensemble/{ensemble.ensemble_uuid}',
        f'{hypervector.API_BASE}/benchmark/{benchmark.benchmark_uuid}',
    ]

    for endpoint in endpoints:
        responses.add(responses.DELETE, endpoint + "/delete", "", status=200)
        responses.add(responses.GET, endpoint, status=404)

    hypervector.Benchmark.delete(benchmark.benchmark_uuid)
    with pytest.raises(HypervectorError) as error:
        hypervector.Benchmark.get(benchmark.benchmark_uuid)
        assert error.status_code == 404

    hypervector.Ensemble.delete(ensemble.ensemble_uuid)
    with pytest.raises(HypervectorError) as error:
        hypervector.Ensemble.get(ensemble.ensemble_uuid)
        assert error.status_code == 404

    hypervector.Definition.delete(definition.definition_uuid)
    with pytest.raises(HypervectorError):
        hypervector.Definition.get(definition.definition_uuid)
        assert error.status_code == 404






