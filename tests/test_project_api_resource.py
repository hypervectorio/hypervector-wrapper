import responses

import hypervector
from tests.util import get_resource_path


def test_project_list(mocked_resources, mocked_responses):
    project, _, _, _ = mocked_resources

    mocked_responses.add(
        responses.GET,
        f'{hypervector.API_BASE}/projects',
        json=[
            project.to_response(),
            project.to_response(),
            project.to_response()
        ]
    )

    retrieved_projects = hypervector.Project.list()

    for retrieved_project in retrieved_projects:
        assert isinstance(retrieved_project, hypervector.Project)


def test_project_new(mocked_resources):
    project, _, _, _ = mocked_resources

    project = hypervector.Project.new()

    assert isinstance(project, hypervector.Project)