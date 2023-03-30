from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapSource, MapMarker

class MapMainApp(App):
    
    def build(self):
        box_layout = BoxLayout()
        map_view = MapView(lat = 50.3, lon = 3.05, zoom = 13)
        map_view.map_source = "osm"
        map_marker = MapMarker()
        map_marker.lat = 50.3
        map_marker.lon = 3.05
        box_layout.add_widget(map_view)
        box_layout.add_widget(map_marker)
        return box_layout
    
if __name__ == "__main__":
    MapMainApp().run()