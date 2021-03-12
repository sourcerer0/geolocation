from geolocation.tz import Timezones

class TestTimezones():
    somewhere = Timezones()

    def test_timezone(self):
        assert self.somewhere.timezone == self.somewhere._Timezones__timezone

    def test_set_timezone(self):
        assert self.somewhere.set_timezone((-22.9110137, -43.2093727)) == {'name': 'Rio de Janeiro', 'distance': 2.8266190065246817, 'tz': 'America/Sao_Paulo'}
