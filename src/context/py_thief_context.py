from context.py_thief_args import PyThiefArgs
from services.storage import Storage
from services.talkback import Talkback


class PyThiefContext:
    def __init__(self, args: PyThiefArgs, storage: Storage, talkback: Talkback):
        self._args = args
        self._storage = storage
        self._talkback = talkback

    @property
    def args(self) -> PyThiefArgs:
        return self._args

    @property
    def storage(self) -> Storage:
        return self._storage

    @property
    def talkback(self) -> Talkback:
        return self._talkback
