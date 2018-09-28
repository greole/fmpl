import os
import re


class Folder():

    def __init__(self, path):
        self.path = path


class Case(Folder):

    def __init__(self, path):

        super().__init__(path)
        self.folder = {
                "constant": Folder(os.path.join(self.path, "constant")),
                "system": Folder(os.path.join(self.path, "system"))
            }

    def __getattr__(self, key):
        """ returns Folder or DictionaryFile """
        subFolder = self.folder.get(key)
        if subFolder:
            return subFolder


class DictionaryFile():

    def __init__(self, path):
        self.path = path
        # TODO open file lazy and cache contents
        self.content = self.read_file()

    def read_file(self):
        with open(self.path) as f:
            return f.readlines()

    def _get_raw(self, key):
        return re.findall("{}[ ]?(\w);", self.content)

    def get(self, key, dtype=int, default=None):
        raw = self._get_raw(key)
        if raw:
            return dtype(raw[-1])
        else:
            default


class Dictionary():

    def __init__(self, name):
        self.name = name

