import responses
import hypervector
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


def test_definition_new(mocked_resources):
    project, _, _, _ = mocked_resources

    definition = hypervector.Definition.new(
        definition_file=get_resource_path("hyperdef.json"),
        project_uuid=project.project_uuid
    )

    assert definition.definition_name == "Mocked definition"

