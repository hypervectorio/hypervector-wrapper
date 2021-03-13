class APIKeyNotSetError(Exception):
    pass


class HypervectorError(Exception):
    def __init__(self, response=None):
        self.response = response
        self.status_code = response.status_code




