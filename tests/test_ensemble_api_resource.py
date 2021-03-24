import responses
import hypervector
from hypervector.resources.core.ensemble import EnsembleResult


def test_ensemble_list(mocked_resources, mocked_responses):
    _, definition, ensemble, _ = mocked_resources

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}/ensembles',
        json=[
            ensemble.to_response(),
            ensemble.to_response(),
            ensemble.to_response()
        ]
    )

    retrieved_ensembles = hypervector.Ensemble.list(definition)

    for retrieved_ensemble in retrieved_ensembles:
        assert isinstance(retrieved_ensemble, hypervector.Ensemble)
        assert retrieved_ensemble.ensemble_uuid == ensemble.ensemble_uuid
        assert retrieved_ensemble.definition_uuid == definition.definition_uuid


def test_ensemble_new(mocked_resources):
    _, definition, _, _ = mocked_resources

    ensemble = hypervector.Ensemble.new(
        definition_uuid=definition.definition_uuid,
        size="MEDIUM"
    )

    assert isinstance(ensemble, hypervector.Ensemble)


def test_ensemble_get(mocked_resources):
    _, _, ensemble, _ = mocked_resources

    retrieved_ensemble = hypervector.Ensemble.get(ensemble.ensemble_uuid)

    assert isinstance(retrieved_ensemble, hypervector.Ensemble)