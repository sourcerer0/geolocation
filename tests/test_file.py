from geolocation.types.files import ReadOnlyFile


class TestFile:
    file = ReadOnlyFile("geolocation/data/COORD_DB.txt")

    def test_find_pattern(self):
        assert (self.file.find_pattern("Europe/Andorra")) == 2

    def test_find_pattern_dubai(self):
        assert (self.file.find_pattern("Asia/Dubai")) == 19

    def test_find_pattern_les_escaldes(self):
        assert (self.file.find_pattern("les Escaldes")) == 1

    def test_find_pattern_vienna(self):
        assert (self.file.find_pattern("Europe/Vienna")) == 48

    def test_get_first_line(self):
        assert (
            self.file.get_line(1)
        ) == "les Escaldes\t42.50729\t1.53414\tAD\tEurope/Andorra\n"

    def test_get_random_line(self):
        assert (
            self.file.get_line(378)
        ) == "Sankt Pölten\t48.2\t15.63333\tAT\tEurope/Vienna\n"
