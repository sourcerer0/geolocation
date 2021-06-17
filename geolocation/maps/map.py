import folium

from ..geo_types import Coordinate
from .marker_str import Marker_Store
from ._convert_coordinates import _convert_coordinates_to_list


class Map:
    def __init__(
        self,
        coordinates: Coordinate,
        markers: Marker_Store,
        zoom: int = 20,
        live_marker: bool = True,
    ):
        self._current_view_coordinates = coordinates
        self._map_init(zoom, live_marker)
        self._marker_handler = markers

    def spot(self, coordinates: Coordinate, marker_id: str):
        marker = self._marker_handler.get_marker(marker_id)

        if marker == None:
            return

        marked_location = marker.mark_location(coordinates)

        self._marker_handler.add_marked_place(marked_location)
        marked_location.add_to(self._map_view)

    def update_view_coordinates(self, coordinates: Coordinate):
        self._current_view_coordinates = coordinates
        self._map_view.location = _convert_coordinates_to_list(coordinates)

    def update_map_zoom(self, zoom: int):
        self._map_init(zoom)
        self._mark_saved_locations()

    def render_html_view(self, output_file: str = "index.html"):
        self._map_view.render()
        return self._map_view.save(output_file)

    def _mark_saved_locations(self):
        for marked_place in self._marker_handler.get_marked_locations():
            marked_place.add_to(self._map_view)

    def _map_init(self, zoom: int, live_marker: bool):
        self._map_view = folium.Map(
            location=_convert_coordinates_to_list(self._current_view_coordinates),
            zoom_start=zoom,
            min_zoom=3,
        )

        self._map_view.add_child(folium.LatLngPopup())
        if live_marker:
            self._map_view.add_child(folium.ClickForMarker(popup="Waypoint"))
