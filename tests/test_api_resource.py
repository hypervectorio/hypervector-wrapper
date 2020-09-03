import hypervector


def test_resources():
    projects = hypervector.Project.list()

    assert len(projects) > 0
    assert isinstance(projects[0], hypervector.Project)

    project = hypervector.Project.get(projects[0].project_uuid)

    assert isinstance(project, hypervector.Project)
    assert isinstance(project.definitions[0], hypervector.Definition)
    assert isinstance(project.definitions[0].ensembles[0], hypervector.Ensemble)

    new_project = hypervector.Project.new()

    assert 1 == 1





