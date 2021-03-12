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


def test_resources():
    projects = hypervector.Project.list()

    assert len(projects) > 0

    for project in projects:
        assert isinstance(project, hypervector.Project)

        if project.definitions:
            for definition_meta in project.definitions:
                definition = hypervector.Definition.get(definition_meta.definition_uuid)
                assert isinstance(definition, hypervector.Definition)


def test_delete_resource(test_definition):
    hypervector.Definition.delete(test_definition.definition_uuid)

    x = hypervector.Definition.get(test_definition.definition_uuid)

    assert 1 == 1






