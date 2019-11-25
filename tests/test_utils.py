from aionetbox.utils import singleton


def test_singleton():
    @singleton
    class A(object):
        def __init__(self, *args, **kwargs):
            pass

    obj1 = A(name='Siddhesh')
    obj2 = A(name='Siddhesh', lname='Sathe')
    obj3 = A(name='Siddhesh', lname='Sathe')
    assert obj1 is not obj2, "Created objects must be different"
    assert obj2 is obj3, "Created objects must be same"
