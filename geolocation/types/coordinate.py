class Coordinate:
    def __init__(self, lat: float, lon: float):
        self._lat = lat
        self._lon = lon

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon