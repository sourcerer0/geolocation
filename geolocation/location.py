from geopy.geocoders import Nominatim
from delorean import Delorean

from geolocation.types import Timezones
from geolocation.types import Coordinate
from geolocation.types import Address


class Location:
    def __init__(self, location=None, **kwargs):
        self.__geo_locator = Nominatim(user_agent="geolocator-elleaech")

        self._time = Delorean()
        self._timezone = Timezones()
        self._coordinate = Coordinate

        if location != None:
            self.location = location
            self.timezone = self.coordinates
        else:
            self._location = Address

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, coordinates: Coordinate):
        self._timezone.set_timezone(coordinates)

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
    def location(self, place: str):
        print("Fetching location content...")

        try:
            if type(place) == type(Coordinate(0, 0)):
                nominatim_data = self.__geo_locator.reverse(
                    place(), addressdetails=True, language="en"
                ).raw
            else:
                nominatim_data = self.__geo_locator.geocode(
                    place, addressdetails=True, language="en"
                ).raw

            self._location = Address(nominatim_data)
        except (AttributeError, ValueError):
            print("ERROR ****** Check input and network connection! ******")
            return

        self._coordinate = self._coordinate(
            float(nominatim_data["lat"]), float(nominatim_data["lon"])
        )
