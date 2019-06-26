from django.forms.widgets import TextInput
from django.utils.html import mark_safe


class MapInput(TextInput):
    template_name = "mapbox_location_field\map_input.html"

    class Media:
        js = ("js\map_input.js",)
        css = {
            "all": ("css\map_input.css",)
        }

    def get_context(self, name, value, attrs):
        attrs.update({
            "class": "js-mapbox-input-location-field",
        })

        return super().get_context(name, value, attrs)
