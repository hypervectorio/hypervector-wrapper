import json

import requests

import hypervector
from hypervector.resources.auxilliary.revision import Revision
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

    def refresh(self):
        definition = self.get(self.definition_uuid)
        self.__dict__.update(definition.__dict__)

    @classmethod
    def list(cls):
        endpoint = f"{hypervector.API_BASE}/definitions"
        response = cls.request(endpoint)
        return [cls.from_response(definition) for definition in response]

    @classmethod
    def new(cls, definition, project_uuid=None):
        endpoint = f"{hypervector.API_BASE}/{cls.resource_name}/add"

        if isinstance(definition, dict):
            definition_json = definition
        else:
            definition_json = _parse_definition_from_json_file(definition)

        data = {
            "definition": definition_json,
            "project_uuid": project_uuid
        }

        response = cls.request(endpoint, method=requests.post, json=data)
        return cls.from_response(response)

    def history(self):
        endpoint = f"{hypervector.API_BASE}/definition/{self.definition_uuid}/history"
        response = requests.get(endpoint, headers=self.get_headers()).json()
        history = [Revision.from_response(response_item) for response_item in response]
        return history


def _parse_definition_from_json_file(definition_json_file):
    return json.load(open(definition_json_file, 'rb'))


def _parse_ensembles(ensembles):
    if not ensembles or len(ensembles) == 0:
        return None

    parsed_ensembles = []
    for ensemble in ensembles:
        parsed_ensemble = Ensemble.from_response(ensemble)
        parsed_ensembles.append(parsed_ensemble)
    return parsed_ensembles
