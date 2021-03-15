import responses
import hypervector
from tests.util import get_resource_path
from hypervector.resources.core.definition import _parse_definition_from_json_file


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

    definitions = hypervector.Definition.list()

    for definition in definitions:
        assert isinstance(definition, hypervector.Definition)


def test_definition_new(test_project):
    definition = hypervector.Definition.new(
        definition_file=get_resource_path("hyperdef.json"),
        project_uuid=test_project.project_uuid
    )

    definition_loaded_directly = _parse_definition_from_json_file(get_resource_path("hyperdef.json"))

    assert definition_loaded_directly['definition_name'] == definition.definition_name
