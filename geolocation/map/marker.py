from json import dumps

import folium
from geolocation import Location
from geolocation.map import _Icon
from geolocation.types import Address, Coordinate
from geolocation.map import _convert_coordinates_to_list


class _Marker:
    def __init__(self, color: str, icon_type: str, inside_color: str):
        self._tooltip = "Click me!"
        self._icon = _Icon(color, icon_type, inside_color=inside_color)

    def mark_location(self, coordinates: Coordinate):
        marker_address = self._get_marker_address(coordinates)
        marker_address = self._convert_address_to_popup(marker_address)

        return folium.Marker(
            _convert_coordinates_to_list(coordinates),
            tooltip=self._tooltip,
            popup=marker_address,
            icon=self._icon(),
        )

    def _get_marker_address(self, coordinates: Coordinate):
        marker_address = Location(coordinates)
        return marker_address.location

    def _convert_address_to_popup(self, address: Address):
        popup = dumps(address.get_address()).split('"')
        popup_formatted = ""

        count = 1
        while count < len(popup):
            popup_formatted += "{}: {}\n".format(popup[count], popup[count + 2])
            count += 4

        return popup_formatted
