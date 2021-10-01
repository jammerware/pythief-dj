from os import path


class ParsedArgs:
    def __init__(self, args_dict: dict):
        self._text = None if 'text' not in args_dict else args_dict['text']
        self._videos = None if 'videos' not in args_dict else args_dict['videos']

        # i'm setting defaults for these with argparse, so I'm assuming it's there for now
        self._format = args_dict['format']
        self._out_dir = args_dict['out_dir']

        # this one is calculated but useful
        self._out_dir_mp3 = path.join(self._out_dir, self._format)

    def is_valid(self):
        return (self._videos is not None and len(self._videos) > 0) or self._text is not None

    @property
    def format(self) -> str: return self._format

    @property
    def out_dir(self): return self._out_dir

    # @out_dir.setter
    # def out_dir(self, value):
    #     self._out_dir = value

    @property
    def out_dir_mp3(self): return self._out_dir_mp3

    @property
    def videos(self): return self._videos

    # @videos.setter
    # def videos(self, value):
    #     self._videos = value

    @property
    def text(self): return self._text

    # @text.setter
    # def text_file(self, value):
    #     self._text = value
