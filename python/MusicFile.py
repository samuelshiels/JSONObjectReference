from File import File as f

class MusicFile(f):
    _defaults = {
        "tags": [],
        "artwork": []
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
    def __str__(self) -> str:
        return f"{self.fileName} {self.path} {self.tags}"