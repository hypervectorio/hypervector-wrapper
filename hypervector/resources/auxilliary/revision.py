from hypervector.resources.abstract.api_resource import APIResource


class Revision(APIResource):
    resource_name = 'revision'

    def __init__(self, revision_uuid, added, features):
        self.revision_uuid = revision_uuid
        self.added = added
        self.features = features

    @classmethod
    def from_response(cls, dictionary):
        return cls(
            revision_uuid=dictionary['revision_uuid'],
            added=dictionary['added'],
            features=dictionary['features']
        )

    def to_response(self):
        return {
            "revision_uuid": self.revision_uuid,
            "added": self.added,
            "features": self.features
        }
