import requests

import hypervector
from hypervector.resources.core.definition import Definition
from hypervector.resources.abstract.api_resource import APIResource


class Project(APIResource):
    resource_name = "project"

    def __init__(self, project_uuid, project_name, added=None, definitions=None):
        self.project_uuid = project_uuid
        self.project_name = project_name
        self.added = added
        self.definitions = definitions

    @classmethod
    def from_response(cls, dictionary):
        return cls(project_uuid=dictionary['project_uuid'],
                   project_name=dictionary['project_name'],
                   added=dictionary['added'],
                   definitions=_parse_definitions(dictionary['definitions']))

    def to_response(self):
        return {
            "project_uuid": self.project_uuid,
            "project_name": self.project_name,
            "added": self.added,
            "definitions": self.definitions
        }

    @classmethod
    def from_get(cls, response):
        return cls.from_response(response.json())

    def refresh(self):
        project = self.get(self.project_uuid)
        self.__dict__.update(project.__dict__)

    @classmethod
    def list(cls):
        endpoint = f"{hypervector.API_BASE}/projects"
        response = cls.request(endpoint)
        return [cls.from_response(project) for project in response]

    @classmethod
    def new(cls):
        endpoint = hypervector.API_BASE + "/" + cls.resource_name + "/new"
        response = requests.post(endpoint, headers=cls.get_headers()).json()

        return cls.from_response(response)


def _parse_definitions(definitions):
    parsed_definitions = []
    for definition in definitions:
        parsed_definition = Definition.from_response(definition)
        parsed_definitions.append(parsed_definition)
    return parsed_definitions








