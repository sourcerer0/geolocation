from json import dumps

import folium

from .. import Location
from ..geo_types import Address, Coordinate
from ._convert_coordinates import _convert_coordinates_to_list
from .icon import _Icon


class _Marker:
    def __init__(self, color: str, icon_type: str, inside_color: str, id_prefix: str):
        self._tooltip = "Click me!"
        self._icon = _Icon(
            color, icon_type, inside_color=inside_color, prefix=id_prefix
        )

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
        popup_msg = dumps(address.get_address(), ensure_ascii=False).split('"')
        popup_formatted = ""

        count = 1
        while count < len(popup_msg) - 4:
            popup_formatted += "{}:<br>{}<br><br>".format(
                popup_msg[count].upper(),
                popup_msg[count + 2],
            )
            count += 4

        iframe = folium.IFrame(popup_formatted, width=200, height=280)
        popup = folium.Popup(iframe, max_width=200)

        return popup
