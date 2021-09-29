class ParsedArgs:
    def __init__(self):
        self._out_dir = None
        self._videos = None

    @property
    def out_dir(self): return self._out_dir

    @out_dir.setter
    def set_out_dir(self, value):
        self._out_dir = value

    @property
    def videos(self): return self._videos

    @videos.setter
    def set_videos(self, value):
        self._videos = value

    def is_valid(self):
        return self._videos is not None and len(self._videos) > 0
