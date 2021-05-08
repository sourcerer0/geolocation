from geolocation.tzone import Timezones
from geolocation import Location


class TestTimezones:
    somewhere = Timezones()

    def test_set_timezone(self):
        geo = Location("Rio de Janeiro, Rio de Janeiro, Brasil")
        assert self.somewhere.set_timezone(geo.coordinates) == {
            "name": "Rio de Janeiro",
            "distance": 2.8266190065246817,
            "tz": "America/Sao_Paulo",
        }
