from os import path


class PyThiefArgs:
    @classmethod
    def from_kwargs(cls, args_dict: dict[str, str]):
        args = PyThiefArgs()
        args._txt = None if 'text' not in args_dict else args_dict['txt']
        args._videos = [] if 'video' not in args_dict else list(args_dict['video'])

        # i'm setting defaults for these with click, so I'm assuming it's there for now
        args._format = args_dict['format'].lower()
        args._keep_raw = args_dict['keep_raw']
        args._out_dir = args_dict['out_dir']

        # they can pass videos as unnamed arguments too
        args._videos += list(args_dict['videos'])

        return args

    @property
    def format(self) -> str: return self._format

    @property
    def out_dir(self): return self._out_dir

    @property
    def keep_raw(self): return self._keep_raw

    @property
    def txt(self): return self._txt

    @property
    def videos(self): return self._videos

    @property
    def is_valid(self):
        return (self._txt is not None and self._txt != '') or (self._videos is not None and len(self._videos) > 0)
