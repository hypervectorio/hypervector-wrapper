import uuid

import responses
import hypervector
from hypervector.resources.auxilliary.revision import Revision
from tests.util import get_resource_path


def test_definition_list(mocked_resources, mocked_responses):
    _, definition, _, _ = mocked_resources

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definitions',
        json=[
            definition.to_response(),
            definition.to_response(),
            definition.to_response()
        ]
    )

    retrieved_definitions = hypervector.Definition.list()

    for retrieved_definition in retrieved_definitions:
        assert isinstance(retrieved_definition, hypervector.Definition)
        assert retrieved_definition.definition_uuid == definition.definition_uuid


def test_definition_new_from_dict(mocked_resources):
    project, _, _, _ = mocked_resources

    definition_dict = {
        "definition_name": "Test definition",
        "features": [
            {
                "type": "float",
                "distribution": {
                    "type": "gaussian",
                    "mu": 1E-2,
                    "sigma": 1.5
                }
            }
        ]
    }

    definition = hypervector.Definition.new(
        definition=definition_dict,
        project_uuid=project.project_uuid
    )

    assert isinstance(definition, hypervector.Definition)


def test_definition_new_from_file(mocked_resources):
    project, _, _, _ = mocked_resources

    definition = hypervector.Definition.new(
        definition=get_resource_path("hyperdef.json"),
        project_uuid=project.project_uuid
    )

    assert isinstance(definition, hypervector.Definition)


def test_definition_ensembles(mocked_resources, mocked_responses):
    _, definition, ensemble, _ = mocked_resources

    definition_response = definition.to_response()
    definition_response['ensembles'] = [
        ensemble.to_response(),
        ensemble.to_response(),
        ensemble.to_response()
    ]

    mocked_responses.replace(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}',
        json=definition_response
    )

    definition = hypervector.Definition.get(definition.definition_uuid)

    for ensemble_from_response in definition.ensembles:
        assert isinstance(ensemble_from_response, hypervector.Ensemble)
        assert len(ensemble_from_response.hypervectors()) == ensemble.size


def test_definition_history(mocked_resources, mocked_responses):
    _, definition, _, _ = mocked_resources

    mocked_revision = Revision(
        revision_uuid=str(uuid.uuid4()),
        added="01/01/1970 00:00:01",
        features=[]
    )

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/definition/{definition.definition_uuid}/history',
        json=[mocked_revision.to_response()]
    )

    history = definition.history()

    for revision in history:
        assert isinstance(revision, Revision)

