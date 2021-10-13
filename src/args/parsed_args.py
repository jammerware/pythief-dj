from os import path


class ParsedArgs:
    @classmethod
    def from_kwargs(cls, args_dict: dict[str, str]):
        args = ParsedArgs()
        args._txt = None if 'text' not in args_dict else args_dict['txt']
        args._videos = None if 'video' not in args_dict else list(args_dict['video'])

        # i'm setting defaults for these with argparse, so I'm assuming it's there for now
        args._format = args_dict['format']
        args._keep_raw = 'keep_raw' in args_dict
        args._out_dir = args_dict['out_dir']

        return args

    @property
    def format(self) -> str: return self._format

    @property
    def out_dir(self): return self._out_dir

    @property
    def keep_raw(self): return self._keep_raw

    @property
    def out_dir_mp3(self): return self._out_dir_mp3

    @property
    def txt(self): return self._txt

    @property
    def videos(self): return self._videos

    @property
    def is_valid(self):
        return (self._txt is not None and self._txt != '') or (self._videos is not None and len(self._videos) > 0)
