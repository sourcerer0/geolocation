from geopy.distance import great_circle

class Timezones():
    def __init__(self, tz = "UTC"):
        self.__timezone = tz

        self.__file = open("geolocation/tz/COORD_DB.txt", "r")

    def set_timezone(self, coordinates):
        if type(coordinates) != type(()):
            print("ERROR ****** Coordinates not accepted!******")
            return

        for lines in self.__file.readlines():
            pass

        return self.__timezone

    @property
    def timezone(self):
        return self.__timezone

    def __repr__(self):
        return "Timezone: {}".format(self.__timezone)