class File:
    def __init__(self, file_name):
        self._access_type = "r"
        self._file = open(file_name, self._access_type)

    @property
    def file(self):
        return self._file

    def reset_read(self):
        self._file.seek(0)

    def read(self):
        return self._file.readlines()