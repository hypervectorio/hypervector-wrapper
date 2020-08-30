import hypervector


def test_list_resources():
    hypervector.API_KEY = "PlfoV2peBisiCmAegiHsW-LxXnpYRcrXw0nGSko6s3iLEnc"

    projects = hypervector.Project.list()

    assert len(projects) > 0
    assert isinstance(projects[0], hypervector.Project)

    project = hypervector.Project.get(projects[0].project_uuid)

    assert isinstance(project, hypervector.Project)
