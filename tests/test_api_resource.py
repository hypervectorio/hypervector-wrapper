import uuid
import pytest
import responses

import hypervector
from hypervector.errors import APIKeyNotSetError, HypervectorError


def test_no_api_key(monkeypatch):
    def mock_empty_api_key():
        return None

    monkeypatch.setattr(hypervector, 'API_KEY', mock_empty_api_key())

    with pytest.raises(APIKeyNotSetError):
        hypervector.Project.list()


def test_get_resource(mocked_resources):
    _, definition, _, _ = mocked_resources

    retrieved_definition = hypervector.Definition.get(definition.definition_uuid)

    assert retrieved_definition.definition_uuid == definition.definition_uuid


def test_get_resource_not_found(mocked_responses):
    random_resource_uuid = str(uuid.uuid4())

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{random_resource_uuid}',
        status=404
    )

    with pytest.raises(HypervectorError) as error:
        hypervector.Definition.get(random_resource_uuid)
        assert error.status_code == 404


def test_delete_resource(mocked_resources, mocked_responses):
    _, definition, ensemble, benchmark = mocked_resources

    endpoints = [
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}',
        f'{hypervector.API_BASE}/ensemble/{ensemble.ensemble_uuid}',
        f'{hypervector.API_BASE}/benchmark/{benchmark.benchmark_uuid}',
    ]

    for endpoint in endpoints:
        mocked_responses.add(responses.DELETE, endpoint + "/delete", "", status=200)
        mocked_responses.replace(responses.GET, endpoint, status=404)

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






