import hypervector


def test_project_creation():
    new_project = hypervector.Project.new()

    assert isinstance(new_project, hypervector.Project)