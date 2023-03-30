from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapSource, MapMarker

class MapMainApp(App):
    
    def build(self):
        box_layout = BoxLayout()
        map_view = MapView(lat = 50.3, lon = 3.05, zoom = 13)
        map_view.map_source = "osm"
        localizacao_usuario = MapMarker(lon = 3.05, lat = 50.3)
        localizacao_usuario.source = "marker_pequeno.png"
        localizacao_usuario.size_hint = (0.2, 0.2)
        map_view.add_marker(localizacao_usuario)
        box_layout.add_widget(map_view)
        return box_layout
    
if __name__ == "__main__":
    MapMainApp().run()