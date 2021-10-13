from os import path
import pathlib
import shutil


class Storage:
    @classmethod
    def from_out_root(cls, root: str):
        storage = Storage()
        storage._root = path.abspath(root)

        # computed paths
        storage._raw_root = path.join(root, 'raw')

        # create missing paths
        pathlib.Path(storage._raw_root).mkdir(parents=True, exist_ok=True)

        return storage

    @property
    def root(self): return self._root

    @property
    def raw_root(self): return self._raw_root

    def delete_raw(self):
        shutil.rmtree(self._raw_root)
