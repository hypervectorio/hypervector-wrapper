class APIKeyNotSetError(Exception):
    pass


class APIBaseError(Exception):
    pass


class HypervectorError(Exception):
    def __init__(self, response=None):
        self.response = response
        if response:
            self.status_code = response.status_code
        else:
            self.status_code = None




