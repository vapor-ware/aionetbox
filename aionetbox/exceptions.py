
class AIONetboxException(Exception):
    pass


class MissingRequiredParam(AIONetboxException):
    pass


class BadRequest(AIONetboxException):
    pass


class InvalidResponse(AIONetboxException):
    pass


class InvalidRequest(AIONetboxException):
    pass
