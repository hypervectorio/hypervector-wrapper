class APIKeyNotSetError(Exception):
    pass


class HypervectorError(Exception):
    def __init__(self, response=None):
        self.response = response
        self.status_code = response.status_code


class ResourceNotFoundError(HypervectorError):
    def __init__(self, response=None):
        super(ResourceNotFoundError, self).__init__(response)



