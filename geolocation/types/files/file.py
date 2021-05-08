class File:
    def __init__(self, file_name):
        self._file = open(file_name)

    @property
    def file(self):
        return self._file

    def find_pattern(self, line_pattern: str):
        number_of_occurrencies = 0

        for line, content in enumerate(self.read()):
            if line_pattern in content:
                print("{}\t{}".format((line + 1), content))
                number_of_occurrencies += 1
        return number_of_occurrencies

    def get_line(self, input_line: int):
        input_line -= 1
        for position, content in enumerate(self.read()):
            if position == input_line:
                return content

    def read(self, lines_number=-1):
        self.reset_read()
        return self._file.readlines(lines_number)

    def reset_read(self):
        self._file.seek(0)


class ReadOnlyFile(File):
    def __init__(self, file_name):
        self.__access_type = "r"
        self._file = open(file_name, self.__access_type)
