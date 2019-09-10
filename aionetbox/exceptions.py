
class AIONetboxException(Exception):
    """ The base exception class to which you can subscribe
    and dont forget to hit the little bell icon to get notified
    of all my new releases."""
    pass


class NoResultsException(AIONetboxException):
    """ Raised when the 'results' key is not present in the json response. """
    pass
