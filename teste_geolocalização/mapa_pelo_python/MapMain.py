from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.mapview import MapView, MapSource, MapMarker
from geopy.geocoders import Nominatim

class Aplicativo(App):
    pass

class GerenciarTelas(ScreenManager):
    pass

class TelaLogin(Screen):
    pass

class TelaMapa(Screen):
    def build(self):
        usuario_localizacao = self.get_location()
        print (f"longitude {usuario_localizacao.longitude} \n latitude {usuario_localizacao.latitude} ")
        
        box_layout = BoxLayout()
        map_view = MapView(lon = usuario_localizacao.longitude, lat = usuario_localizacao.latitude, zoom = 13)
        map_view.map_source = "osm"
        
        usuario_marker = MapMarker(lon = usuario_localizacao.longitude, lat = usuario_localizacao.latitude)
        usuario_marker.source = "marker_pequeno.png"
        map_view.add_marker(usuario_marker)
        box_layout.add_widget(map_view)
        
        return box_layout
    
    def get_location(self):
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode("my_location")

        return location
    
    
if __name__ == "__main__":
    Aplicativo().run()