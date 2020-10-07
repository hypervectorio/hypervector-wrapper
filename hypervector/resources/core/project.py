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

        if 'definitions' not in dictionary.keys():
            return cls(project_uuid=dictionary['project_uuid'],
                       project_name=dictionary['project_name'])

        return cls(project_uuid=dictionary['project_uuid'],
                   project_name=dictionary['project_name'],
                   added=dictionary['added'],
                   definitions=_parse_definitions(dictionary['definitions']))

    @classmethod
    def from_response_get(cls, dictionary):
        return cls.from_response(dictionary)

    @classmethod
    def new(cls):
        endpoint = hypervector.API_BASE + "/" + cls.resource_name + "/new"
        response = requests.post(endpoint, headers=cls.get_headers()).json()

        return cls.from_response(response)


def _parse_definitions(definitions):
    parsed_definitions = []
    for definition_uuid, definition_meta in definitions.items():
        parsed_definition = Definition.from_dict(definition_uuid, definition_meta)
        parsed_definitions.append(parsed_definition)
    return parsed_definitions








