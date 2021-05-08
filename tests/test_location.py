from geolocation.types.coordinate import Coordinate
from geolocation import Location


class TestLocation:
    somewhere = Location("San José, California, USA")

    def test_timezone(self):
        assert self.somewhere.timezone == self.somewhere._timezone

    def test_location_getter(self):
        assert self.somewhere.location == self.somewhere._location
