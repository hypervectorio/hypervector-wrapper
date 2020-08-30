from hypervector.resources.abstract.api_resource import APIResource


class Project(APIResource):

    def __init__(self):
        self.resource_name = "project"