from asynctest import CoroutineMock
from unittest.mock import MagicMock


class AIONetboxMock:
    @classmethod
    def from_openapi(cls, *args, **kwargs):
        return cls()

    @classmethod
    def from_spec(cls, *args, **kargs):
        return cls()

    def __init__(self):
        self._endpoints = {}

    def __getattr__(self, name):
        if name not in self._endpoints:
            self._endpoints[name] = AIONetboxEndpointMock()

        return self._endpoints.get(name)


class AIONetboxEndpointMock:
    def __init__(self):
        self._endpoints = {}

    def __getattr__(self, name):
        if name not in self._endpoints:
            self._endpoints[name] = CoroutineMock(return_value=MagicMock())

        return self._endpoints.get(name)

    def __call__(self, name):
        return self.__getattr__(name)
