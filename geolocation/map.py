from geolocation.types.address import Address
from geolocation.types import Coordinate
from geolocation import Location
from folium import folium

from json import dumps


class Map:
    def __init__(self, coordinates: Coordinate, zoom=20, location_data=None):
        if location_data != None:
            self._location_data = Location(coordinates)
        else:
            self._location_data = None

        self._initial_coordinates = coordinates
        self._map_view = folium.Map(
            location=self._convert_coordinates_to_list(), zoom_start=zoom
        )

        self._tooltip = "Click me!"
        # icons

    def update_coordinates(self, coordinates: Coordinate):
        self._initial_coordinates = coordinates

    def render_html_view(self):
        self._map_view.render()
        return self._map_view.save("index.html")

    # ADD TYPE OF LOCATION MARK
    def mark_location(self, coordinates: Coordinate):
        marker_address = self._get_marker_address(coordinates)
        marker_address = self._convert_address_to_popup(marker_address)

        folium.Marker(
            self._convert_coordinates_to_list(coordinates),
            tooltip=self._tooltip,
            popup=marker_address,
            icon=folium.Icon(),  ############
        ).add_to(self._map_view)

    def _get_marker_address(self, coordinates: Coordinate):
        marker_address = Location(Coordinate)
        return marker_address.location

    def _convert_address_to_popup(self, address: Address):
        popup = dumps(address.get_address()).split('"')
        popup_formatted = ""

        count = 1
        while count < len(popup):
            popup_formatted += "{}: {}\n".format(popup[count], popup[count + 2])
            count += 4

        return popup_formatted

    def _convert_coordinates_to_list(self, coordinates: Coordinate = None):
        if coordinates == None:
            list(self._initial_coordinates.coordinates())
        else:
            return list(coordinates)
