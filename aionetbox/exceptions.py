
class AIONetboxException(Exception):
    pass


class MissingRequiredParam(AIONetboxException):
    pass


class BadRequest(AIONetboxException):
    pass


class ClientFilterError(AIONetboxException):
    def __init__(self, message):
        self.context = message


class InvalidResponse(AIONetboxException):
    pass


class InvalidRequest(AIONetboxException):
    pass
