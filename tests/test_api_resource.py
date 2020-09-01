import hypervector


def test_resources():
    hypervector.API_KEY = "qRokv-vMqeHy7vkgsLEOgJitIRBP-N9b-zo81UCcPrlkzMA"

    projects = hypervector.Project.list()

    assert len(projects) > 0
    assert isinstance(projects[0], hypervector.Project)

    project = hypervector.Project.get(projects[0].project_uuid)

    assert isinstance(project, hypervector.Project)
    assert isinstance(project.definitions[0], hypervector.Definition)
    assert isinstance(project.definitions[0].ensembles[0], hypervector.Ensemble)



