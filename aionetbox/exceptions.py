
class AIONetboxException(Exception):
    pass


class MissingRequiredParam(AIONetboxException):
    pass


class BadRequest(AIONetboxException):
    pass


class ClientFilterError(AIONetboxException):
    def __init__(self, message, status, request_info):
        self.context = message
        self.status = status
        self.request_info = request_info


class InvalidResponse(AIONetboxException):
    pass


class InvalidRequest(AIONetboxException):
    pass
