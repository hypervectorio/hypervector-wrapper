import hypervector
from tests.util import get_resource_path


def test_project_creation():
    new_project = hypervector.Project.new()

    assert isinstance(new_project, hypervector.Project)

    new_definition = hypervector.Definition.new(project_uuid=new_project.project_uuid,
                                                definition_file=get_resource_path("hyperdef.json"))

    assert isinstance(new_definition, hypervector.Definition)