from geopy.geocoders import Nominatim
from delorean import Delorean

from geolocation.tzone import Timezones
from geolocation.types import Coordinate


class Location:
    def __init__(self, location=None, **kwargs):
        self.__geo_locator = Nominatim(user_agent="geolocator-elleaech")

        self._time = Delorean()
        self._timezone = Timezones()
        self._coordinate = Coordinate

        if location != None:
            self.location = location
        else:
            self._location = {}

    @property
    def timezone(self):
        return self._timezone

    @property
    def time(self):
        return self._time.now().shift(self._timezone.timezone)

    @property
    def format_time(self):
        return self.time.format_datetime()

    @property
    def coordinates(self):
        return self._coordinate

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, place):
        try:
            if type(place) == type(Coordinate(0.0, 0.0)):
                self._location = self.__geo_locator.reverse(
                    (place.lat, place.lon), addressdetails=True, language="en"
                ).raw
            elif type(place) == type(""):
                self._location = self.__geo_locator.geocode(
                    place, addressdetails=True, language="en"
                ).raw

        except AttributeError:
            print("ERROR ****** Check place and network connection! ******")
            return
        except ValueError:
            print(
                "ERROR ****** Please, provide a valid coordinate and try again! ******"
            )
            return

        self._coordinate = Coordinate(
            float(self._location["lat"]), float(self._location["lon"])
        )
