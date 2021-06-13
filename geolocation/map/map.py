from geolocation.types import Coordinate
from geolocation.map import _Marker
from geolocation.map import _convert_coordinates_to_list
import folium


class Map:
    def __init__(self, coordinates: Coordinate, zoom: int = 20):
        self._initial_coordinates = coordinates
        self._map_view = folium.Map(
            location=_convert_coordinates_to_list(self._initial_coordinates),
            zoom_start=zoom,
        )

    def spot(
        self, coordinates: Coordinate, color: str, icon_type: str, inside_color: str
    ):
        marker = _Marker(color, icon_type, inside_color)
        marker.mark_location(coordinates).add_to(self._map_view)

    def update_view_coordinates(self, coordinates: Coordinate, zoom: int = 20):
        self._initial_coordinates = coordinates
        self._map_view = folium.Map(
            location=_convert_coordinates_to_list(coordinates),
            zoom_start=zoom,
        )

    def render_html_view(self, output_file: str = "index.html"):
        self._map_view.render()
        return self._map_view.save(output_file)
