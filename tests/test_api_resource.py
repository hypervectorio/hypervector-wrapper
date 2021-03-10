import hypervector


def test_resources():
    projects = hypervector.Project.list()

    assert len(projects) > 0

    for project in projects:
        assert isinstance(project, hypervector.Project)

        if project.definitions:
            for definition_meta in project.definitions:
                definition = hypervector.Definition.get(definition_meta.definition_uuid)
                assert isinstance(definition, hypervector.Definition)





