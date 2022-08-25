class File(object):
    _defaults = {
        "path": None,
        "fileName": None,
        "fileType": None
    }
    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)    