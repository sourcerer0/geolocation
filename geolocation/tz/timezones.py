from geopy.distance import great_circle


class Timezones:
    def __init__(self, zone="UTC"):
        self.__file = open("geolocation/tz/COORD_DB.txt", "r")

        self.__timezone = zone

    def set_timezone(self, coordinates):
        if type(coordinates) != type(()):
            print("ERROR ****** Coordinates not accepted!******")
            return

        ref_city = {"name": "", "distance": 1000, "tz": ""}
        self.__file.seek(0)

        print("Finding best timezone match...")
        for line in self.__file.readlines():
            LINE = line.split("\t")
            distance = great_circle(coordinates, (float(LINE[1]), float(LINE[2]))).km

            if distance < ref_city["distance"]:
                ref_city["name"] = LINE[0]
                ref_city["distance"] = distance
                ref_city["tz"] = LINE[4].split("\n")[0]

        self.__timezone = ref_city["tz"]

        return ref_city

    @property
    def timezone(self):
        return self.__timezone

    def __repr__(self):
        return "Timezone: {}".format(self.__timezone)