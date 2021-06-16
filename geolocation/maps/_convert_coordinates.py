from ..geo_types import Coordinate


def _convert_coordinates_to_list(coordinates: Coordinate = None):
    return list(coordinates())
