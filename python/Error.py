class Error(object):
    _defaults = {
        'errorCode':'',
        'errorDescription':''
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
