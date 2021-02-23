from geopy.distance import great_circle

class Timezones():
    def __init__(self, tz = "UTC"):
        self.__file = open("geolocation/tz/COORD_DB.txt", "r")

        self.__ref_city = None
        self.__timezone = tz

    def set_timezone(self, coordinates):
        if type(coordinates) != type(()):
            print("ERROR ****** Coordinates not accepted!******")
            return

        ref_city = None
        for lines in self.__file.readlines():
            for line in self.__file.readlines(): line = line.split("\t")
                ## DO SOME SEARCH HERE


        self.__ref_city = (ref_city[1], ref_city[8], ref_city[4], ref_city[5])
        self.__timezone = ref_city[17]

        return self.__timezone

    @property
    def timezone(self):
        return self.__timezone

    def __repr__(self):
        return "Timezone: {}\n".format(self.__timezone)