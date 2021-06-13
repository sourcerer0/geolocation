from geolocation.types.coordinate import Coordinate
from geolocation.types.database import Database
from geopy.distance import great_circle


class Timezones:
    def __init__(self, zone="UTC"):
        self._file = Database()
        self._referencial_place = {"distance": 1000}
        self._timezone = zone

    def __repr__(self):
        return "Timezone: {}".format(self._timezone)

    def set_timezone(self, coordinates: Coordinate):
        if type(coordinates) != type(Coordinate(0, 0)):
            print("ERROR ****** Coordinates not accepted!******")
            return

        self._file.reset_read()
        print("Finding best timezone match...")

        for line in self._file.read():
            line = line.split("\t")

            distance = great_circle(
                (coordinates.lat, coordinates.lon), (float(line[1]), float(line[2]))
            ).km

            if distance < self._referencial_place["distance"]:
                self._referencial_place["name"] = line[0]
                self._referencial_place["distance"] = distance
                self._referencial_place["tz"] = line[4].split("\n")[0]

        self._timezone = self._referencial_place["tz"]

        return self._referencial_place

    @property
    def timezone(self):
        return self._timezone
