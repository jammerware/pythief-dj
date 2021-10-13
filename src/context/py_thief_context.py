from context.py_thief_args import PyThiefArgs
from services.storage import Storage


class PyThiefContext:
    def __init__(self, args: PyThiefArgs, storage: Storage):
        self._args = args
        self._storage = storage

    @property
    def args(self) -> PyThiefArgs:
        return self._args

    @property
    def storage(self) -> Storage:
        return self._storage
