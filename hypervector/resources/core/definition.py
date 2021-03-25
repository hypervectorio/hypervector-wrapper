import json

import requests

import hypervector
from hypervector.resources.core.ensemble import Ensemble
from hypervector.resources.abstract.api_resource import APIResource


class Definition(APIResource):
    resource_name = 'definition'

    def __init__(self, definition_uuid, definition_name, added, ensembles):
        self.definition_uuid = definition_uuid
        self.definition_name = definition_name
        self.added = added
        self.ensembles = ensembles

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            definition_uuid=dictionary['definition_uuid'],
            definition_name=dictionary['definition_name'],
            added=dictionary['added'],
            ensembles=_parse_ensembles(dictionary['ensembles'])
        )

    def to_response(self):
        return {
            "definition_uuid": self.definition_uuid,
            "definition_name": self.definition_name,
            "added": self.added,
            "ensembles": self.ensembles
        }

    @classmethod
    def from_get(cls, response):
        return cls.from_response(response.json())

    @classmethod
    def list(cls):
        endpoint = f"{hypervector.API_BASE}/definitions"
        response = requests.get(endpoint, headers=cls.get_headers()).json()
        return [cls.from_response(definition) for definition in response]

    @classmethod
    def new(cls, definition_file, project_uuid=None):
        endpoint = f"{hypervector.API_BASE}/{cls.resource_name}/add"
        data = {
            "definition": _parse_definition_from_json_file(definition_file),
            "project_uuid": project_uuid
        }
        response = requests.post(endpoint, json=data, headers=cls.get_headers()).json()
        return cls.from_response(response)


def _parse_definition_from_json_file(definition_json_file):
    return json.load(open(definition_json_file, 'rb'))


def _parse_ensembles(ensembles):
    parsed_ensembles = []
    for ensemble in ensembles:
        parsed_ensemble = Ensemble.from_response(ensemble)
        parsed_ensembles.append(parsed_ensemble)
    return parsed_ensembles
