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
    def from_dict_for_lists(cls, dictionary):
        return cls(project_uuid=dictionary['project_uuid'],
                   project_name=dictionary['project_name'])

    @classmethod
    def from_dict(cls, dictionary):
        return cls(project_uuid=dictionary['project_uuid'],
                   project_name=dictionary['project_name'],
                   added=dictionary['added'],
                   definitions=_parse_definitions(dictionary['definitions']))


def _parse_definitions(definitions):
    parsed_definitions = []
    for definition_uuid, definition_meta in definitions.items():
        parsed_definition = Definition.from_dict(definition_uuid, definition_meta)
        parsed_definitions.append(parsed_definition)
    return parsed_definitions








