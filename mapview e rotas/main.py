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
        self.ids.main_map.center_on(self.ids.main_map_me.lat, self.ids.main_map_me.lon)
        
    def press(self):
        print(str(self.ids.main_map_me.lat) + ' | ' + str(self.ids.main_map_me.lon))  
        
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