from hypervector.resources.core.ensemble import Ensemble
from hypervector.resources.abstract.api_resource import APIResource


class Definition(APIResource):
    resource_name = 'definition'

    def __init__(self, definition_uuid, definition_name, ensembles=None):
        self.definition_uuid = definition_uuid
        self.definition_name = definition_name
        self.ensembles = ensembles

    @classmethod
    def from_dict(cls, definition_uuid, dictionary):
        return cls(
            definition_uuid=definition_uuid,
            definition_name=dictionary['definition_name'],
            ensembles=_parse_ensembles(dictionary['ensembles'])
        )


def _parse_ensembles(ensembles):
    parsed_ensembles = []
    for ensemble_uuid, ensemble_meta in ensembles.items():
        parsed_ensemble = Ensemble.from_dict(ensemble_uuid, ensemble_meta)
        parsed_ensembles.append(parsed_ensemble)
    return parsed_ensembles

