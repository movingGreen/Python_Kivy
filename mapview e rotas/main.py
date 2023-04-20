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
        self.placed = False
        self.exists = False
        
    def press(self):
        print(str(self.ids.main_map_me.lat) + ' | ' + str(self.ids.main_map_me.lon)) 
        
         
        
    def place_pin(self):
        self.placed = True
    
    def remove_pin(self):
        if self.exists == True:
            self.ids.main_map.remove_widget(self.dist)
            self.placed = False
            self.exists = False
    
    def on_touch_up(self, touch):
        
        dist_lat, dist_lon = self.ids.main_map.get_latlon_at(touch.x, touch.y)
        
        if touch.y > self.width * 0.05:
            if self.placed == True and self.exists == False:
                self.dist = MapMarkerPopup(lat = dist_lat, lon = dist_lon, source = 'marker_32.png')
                
                self.button = Button(text = 'print loc', on_press = self.press_dist)
                self.dist.add_widget(self.button)
                self.ids.main_map.add_widget(self.dist)
                self.exists = True
                
                print(self.ids.main_map.get_latlon_at(touch.x, touch.y))
        
    def press_dist(self, instance):
        print(f"{self.dist.lat}\n{self.dist.lon}")        
        
        
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