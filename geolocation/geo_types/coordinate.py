class Coordinate:
    def __init__(self, lat: float, lon: float):
        self._lat = lat
        self._lon = lon

    def __call__(self):
        return (self._lat, self._lon)

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon