import folium

from ..geo_types import Coordinate
from ._convert_coordinates import _convert_coordinates_to_list
from .marker import _Marker


class Map:
    def __init__(self, coordinates: Coordinate, zoom: int = 20):
        self._current_coordinates = coordinates
        self._map_init(zoom)

        self._marked_places = list()

    def spot(
        self, coordinates: Coordinate, color: str, icon_type: str, inside_color: str
    ):
        marker = _Marker(color, icon_type, inside_color)
        marked_location = marker.mark_location(coordinates)

        self._marked_places.append(marked_location)
        marked_location.add_to(self._map_view)

    def update_view_coordinates(self, coordinates: Coordinate):
        self._current_coordinates = coordinates
        self._map_view.location = _convert_coordinates_to_list(coordinates)

    def update_map_zoom(self, zoom: int):
        self._map_init(zoom)
        self._mark_saved_locations()

    def render_html_view(self, output_file: str = "index.html"):
        self._map_view.render()
        return self._map_view.save(output_file)

    def _mark_saved_locations(self):
        for marked_place in self._marked_places:
            print("here")
            marked_place.add_to(self._map_view)

    def _map_init(self, zoom: int):
        self._map_view = folium.Map(
            location=_convert_coordinates_to_list(self._current_coordinates),
            zoom_start=zoom,
            min_zoom=3,
        )
