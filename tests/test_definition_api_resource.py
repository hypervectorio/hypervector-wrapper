import pytest
import hypervector
from tests.util import get_resource_path
from hypervector.resources.core.definition import _parse_definition_from_json_file


@pytest.fixture
def test_project():
    project = hypervector.Project.new()
    return project


def test_definition_list():
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
