from kivy.app import App
from kivy_garden.mapview import MapView, MapMarkerPopup, MapMarker, MapSource
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

class telaPrincipal(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.ids.main_map.zoom = 15
        self.ids.main_map.center_on(-15.57, -56.03)

        self.pin = MapMarkerPopup(lat = -15.57, lon = -56.03, source = "marker_pequeno.png")
        self.btn = Button(size = (self.width * .2, self.height * .05), on_press = self.show)
        
        self.pin.add_widget(self.btn)
        self.ids.main_map.add_widget(self.pin)

    def show(self, instance):
        print(str(self.pin.lat,) + ' | ' + str(self.pin.lon))
        
        
class aplicacao(App):
    def build(self):
        self.screen = ScreenManager()
        self.telaP = telaPrincipal()
        screen = Screen(name = 'primeira tela')
        screen.add_widget(self.telaP)
        self.screen.add_widget(screen)
        
        return self.screen
    
if __name__ == "__main__":
    aplicacao().run()