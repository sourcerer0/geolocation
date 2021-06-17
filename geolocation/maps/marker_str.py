from ..geo_types import Coordinate
from .marker import _Marker


class Marker_Store:
    def __init__(self):
        self._marked_places = list()
        self._markers_dictionary = dict()

    def add_new_marker(
        self,
        marker_id: str,
        color: str,
        icon_type: str,
        inside_color: str,
        id_prefix: str,
    ):
        marker = _Marker(color, icon_type, inside_color, id_prefix)
        self._markers_dictionary[marker_id] = marker

    def add_marked_place(self, coordinates: Coordinate, marker_id: str):
        marker = self.get_marker(marker_id)

        if marker == None:
            print("INVALID MARKER ID!")
            return

        marked_location = marker.mark_location(coordinates)

        self._marked_places.append(marked_location)

        return marked_location

    def get_marker(self, marker_id: str):
        if marker_id in self._markers_dictionary:
            marker = self._markers_dictionary[marker_id]
            return marker
        else:
            print("Marker not found!")
            return None

    def get_marked_locations(self):
        return self._marked_places

    def export_markers_to_json(self, output_file: str):
        pass

    def load_markers_from_json(self, input_file: str):
        pass
