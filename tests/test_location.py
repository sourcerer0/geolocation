from geolocation import Location

class TestLocation():
    somewhere = Location("San José, California, USA")

    #def test_up_time(self): assert self.somewhere.up_time() == (self.somewhere._Location__time.now() - self.somewhere._Location__time)

    def test_timezone(self):
        assert self.somewhere.timezone == self.somewhere._Location__timezone

    # def test_time(self): assert self.somewhere.time == self.somewhere._Location__time.now().shift(self.somewhere.timezone.timezone)



    #def test_location_setter(self):
    #   self.somewhere.location = "San José, California, USA"
    #    assert self.somewhere.location == "San José, California, USA"

    def test_location_getter(self):
        assert self.somewhere.location == self.somewhere._Location__location

    def test_coordinates(self):
        assert self.somewhere.coordinates == ((float(self.somewhere._Location__location["lat"]), float(self.somewhere._Location__location["lon"])))
