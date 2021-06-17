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
        self._spotted_location = Location()

    def mark_location(self, coordinates: Coordinate):
        marker_address = self._get_marker_address(coordinates)
        address_time = self._get_address_time()

        popup = self._convert_spotted_location_to_popup(marker_address, address_time)

        return folium.Marker(
            _convert_coordinates_to_list(coordinates),
            tooltip=self._tooltip,
            popup=popup,
            icon=self._icon(),
        )

    def _get_marker_address(self, coordinates: Coordinate):
        self._spotted_location = coordinates
        return self._spotted_location.location

    def _get_address_time(self):
        return self._spotted_location.ftime()

    def _convert_spotted_location_to_popup(self, address: Address, time: str):
        popup_msg = dumps(address.get_address(), ensure_ascii=False).split('"')
        popup_formatted = "{}<br><br>".format(time)

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
