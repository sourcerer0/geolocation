import folium


class _Icon:
    def __init__(self, color: str, icon_type: str, inside_color: str = "white"):
        self.__color_options = [
            "red",
            "blue",
            "green",
            "purple",
            "orange",
            "darkred",
            "lightred",
            "beige",
            "darkblue",
            "darkgreen",
            "cadetblue",
            "darkpurple",
            "white",
            "pink",
            "lightblue",
            "lightgreen",
            "gray",
            "black",
            "lightgray",
        ]

        self._color = color
        self._inside_color = inside_color
        self._icon_type = icon_type

        if self._check_color_options():
            self._icon = folium.Icon(
                color=self._color, color_icon=self._inside_color, icon=self._icon_type
            )

        else:
            return None

    def __call__(self):
        return self._icon

    def _check_color_options(self):
        if (
            self._color in self.__color_options
            and self._inside_color in self.__color_options
        ):
            return True
        else:
            return False
