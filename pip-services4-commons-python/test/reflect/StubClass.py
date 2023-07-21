import datetime


class StubClass:
    _private_field = 123
    public_field = "ABC"
    _public_prop = datetime.datetime.now()

    def __init__(self):
        pass

    def _get_private_prop(self):
        return 543

    def _set_private_prop(self, value):
        pass

    def get_public_prop(self):
        return self._public_prop

    def set_public_prop(self, value):
        self._public_prop = value

    public_prop = property(get_public_prop, set_public_prop)

    def _private_method(self):
        pass

    def public_method(self, arg1, arg2):
        return arg1 + arg2
