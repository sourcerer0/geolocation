from geolocation.types.files import ReadOnlyFile


class TestFile:
    file = ReadOnlyFile("geolocation/data/COORD_DB.txt")

    def test_find_pattern(self):
        assert (self.file.find_pattern("Dubai")) == 20

    def test_get_line(self):
        assert (self.file.get_line(1)) == [
            "les Escaldes",
            "42.50729",
            "1.53414",
            "AD",
            "Europe/Andorra",
        ]
