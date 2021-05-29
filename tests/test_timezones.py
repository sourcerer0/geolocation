from geolocation.tzone import Timezones
from geolocation import Location


class TestTimezones:
    somewhere = Timezones()
    geo = Location

    def test_set_timezone(self):
        geo = self.geo("Rio de Janeiro, Rio de Janeiro, Brasil")
        assert self.somewhere.set_timezone(geo.coordinates)["tz"] == "America/Sao_Paulo"
