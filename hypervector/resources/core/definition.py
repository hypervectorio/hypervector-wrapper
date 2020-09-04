import json

import requests

import hypervector
from hypervector.resources.core.ensemble import Ensemble
from hypervector.resources.abstract.api_resource import APIResource


class Definition(APIResource):
    resource_name = 'definition'

    def __init__(self, definition_uuid, definition_name, added):
        self.definition_uuid = definition_uuid
        self.definition_name = definition_name
        self.added = added

    @classmethod
    def from_dict(cls, definition_uuid, dictionary):
        return cls(
            definition_uuid=definition_uuid,
            definition_name=dictionary['definition_name']
        )

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            definition_uuid=dictionary['definition_uuid'],
            definition_name=dictionary['definition_name'],
            added=dictionary['added']
        )

    @classmethod
    def new(cls, definition_file, project_uuid=None):
        endpoint = f"{hypervector.API_BASE}/{cls.resource_name}"
        data = _parse_definition_from_json_file(definition_file)
        data['project_uuid'] = project_uuid
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)


def _parse_definition_from_json_file(definition_json_file):
    return json.load(open(definition_json_file, 'rb'))

