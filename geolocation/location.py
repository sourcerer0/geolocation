from geopy.geocoders import Nominatim
from delorean import Delorean
from .tz import Timezones


class Location:
    def __init__(self, location=None, **kwargs):
        self._geo_locator = Nominatim(user_agent="geolocator-elleaech")

        self.__time = Delorean()
        self.__timezone = Timezones()

        if location != None:
            self.location = location
        else:
            self.__location = {}

    @property
    def timezone(self):
        return self.__timezone

    @property
    def time(self):
        return self.__time.now().shift(self.timezone.timezone)

    @property
    def format_time(self):
        return self.time.format_datetime()

    @property
    def up_time(self):
        return self.time - self.__time

    @property
    def location(self):
        return self.__location

    @property
    def coordinates(self):
        try:
            return (float(self.location["lat"]), float(self.location["lon"]))
        except TypeError:
            print("Location not defined!")
            return

    @property
    def format_location(self):
        try:
            for key in self.location["address"]:
                print("%s: %s" % (key.upper(), self.location["address"][key]))
        except TypeError:
            print("Location not defined!")
            return

    @location.setter
    def location(self, place):
        try:
            if type(place) == type(()):
                self.__location = self._geo_locator.reverse(
                    place, addressdetails=True, language="en"
                ).raw
            elif type(place) == type(""):
                self.__location = self._geo_locator.geocode(
                    place, addressdetails=True, language="en"
                ).raw
        except AttributeError:
            print("ERROR ****** Check place and network connection! ******")
        except ValueError:
            print(
                "ERROR ****** Please, provide a valid coordinate and try again! ******"
            )
