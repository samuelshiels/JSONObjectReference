class MusicPlaylist():
    _defaults = {
        "files": [],
        "name": []
    }
    def __init__(self, **kwargs):
        """
        :param arr files: List of MusicFile object
        :param str name: Title for the playlist
        """
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)   