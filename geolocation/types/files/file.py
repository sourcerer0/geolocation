class File:
    def __init__(self, file_name):
        self._file = open(file_name)

    @property
    def file(self):
        return self._file

    def find_pattern(self, line_pattern: str):
        self.get_line(1)

        for line, content in enumerate(self.read()):
            if line_pattern in line:
                print("{}\t{}".format((line + 1), content))

    def read(self, line_number=-1):
        self.get_line(1)
        return self._file.readlines(line_number)

    def get_line(self, line: int):
        try:
            self._file.seek((line - 1))
        except:
            return ""
        return self._file.readline()


class ReadOnlyFile(File):
    def __init__(self, file_name):
        self.__access_type = "r"
        self._file = open(file_name, self.__access_type)
