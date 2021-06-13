class Address:
    def __init__(self, Nominatim: dict):
        self._osm = {
            "place_id": Nominatim["place_id"],
            "licence": Nominatim["licence"],
            "osm_type": Nominatim["osm_type"],
            "osm_id": Nominatim["osm_id"],
        }

        self._address = Nominatim["address"]

    def __call__(self):
        for index in self._address:
            print("{}: {}".format(index, self._address[index]))

    def get_address(self):
        return self._address

    def get_osm_data(self):
        print(self._osm["licence"])

        for index in self._osm:
            if index == "licence":
                continue
            print("{}: {}".format(index, self._osm[index]))
