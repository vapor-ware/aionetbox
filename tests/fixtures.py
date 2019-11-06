import asynctest
from unittest.mock import MagicMock


class ResponseMock():

    json = asynctest.CoroutineMock(return_value={})
    raise_for_status = asynctest.CoroutineMock()
    status = 200


class SessionMock(MagicMock):

    request = asynctest.CoroutineMock(return_value=ResponseMock())
    close = asynctest.CoroutineMock()
