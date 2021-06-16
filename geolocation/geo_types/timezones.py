from geopy.distance import great_circle

from .coordinate import Coordinate
from .database import Database


class Timezones:
    def __init__(self, zone="UTC"):
        self._timezones_database = Database("databases/tzones_database.db")

        self._best_match = {"distance": 1000}
        self._timezone = zone

    def __call__(self):
        return self._timezone

    def set_timezone(self, coordinates: Coordinate):
        if type(coordinates) != type(Coordinate(0, 0)):
            print("ERROR ****** Coordinates not accepted!******")
            return

        print("Finding best timezone match...")
        for line in self._timezones_database.get_data_list("timezones_coordinates"):

            distance = great_circle(
                (coordinates.lat, coordinates.lon), (float(line[1]), float(line[2]))
            ).km

            if distance < self._best_match["distance"]:
                self._best_match["name"] = line[0]
                self._best_match["distance"] = distance
                self._best_match["tz"] = line[4]

        self._timezone = self._best_match["tz"]

        return self._best_match
