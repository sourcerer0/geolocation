class Address:
    def __init__(self, Nominatim: dict):
        self._osm = {
            "place_id": Nominatim["place_id"],
            "licence": Nominatim["license"],
            "osm_type": Nominatim["osm_type"],
            "osm_id": Nominatim["osm_id"],
        }

        self._address = Nominatim["address"]

    def __call__(self):
        for index in self._address:
            print("{}: {}\n".format(index, self._address[index]))

    def get_osm_data(self):
        for index in self._osm:
            print("{}: {}\n".format(index, self._osm[index]))
