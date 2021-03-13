from geopy.geocoders import Nominatim
from delorean import Delorean
from .tz import Timezones


class Location():
    def __init__(self, location=None, **kwargs):
        self._geo_locator = Nominatim(user_agent="locator-sourcerer0")

        self.__time = Delorean()
        self.__timezone = Timezones()

        if location != None: self.location = (location)
        else: self.__location = {}

    def up_time(self):
        print(self.__time.now() - self.__time)



    @property
    def timezone(self): return self.__timezone

    @property
    def time(self): return self.__time.now().shift(self.timezone.timezone)

    @property
    def format_time(self): print(self.time.format_datetime())



    @property
    def location(self): return self.__location

    @location.setter
    def location(self, place):
        if type(place) == type(()):
            if (place[0] <= 90 and place[0] >= -90) and (place[1] <= 90 and place[1] >= -90):
                try:
                    self.__location = self._geo_locator.reverse(place, addressdetails=True, language="en").raw
                except AttributeError:
                    print("ERROR ****** Check place input and network connection!******")
            else:
                print("ERROR ****** Coordinates out of range! Must be in the [-90; 90] range.******")
                self.__location = None
        elif type(place) == type(""):
            try:
                self.__location = self._geo_locator.geocode(place, addressdetails=True, language="en").raw
            except AttributeError:
                print("ERROR ****** Check place input and network connection!******")
        else: self.__location = None

    @property
    def coordinates(self): 
        try: return (float(self.location["lat"]), float(self.location["lon"]))
        except TypeError:
            print("Location not defined!")
            return

    @property
    def format_location(self):
        try: print("Coordinates:".upper(), self.location["lat"], self.location["lon"])
        except TypeError:
            print("Location not defined!")
            return

        for key in self.location["address"]: print("%s: %s" % (key.upper(), self.location["address"][key]))
