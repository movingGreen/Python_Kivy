from kivy.app import App
from kivy.garden.mapview import MapMarkerPopup

class MainApp(App):
    latitude = -25
    longitude = -25
    
    def on_start(self):
        marker = MapMarkerPopup(lat = self.latitude, lon = )
    pass

MainApp().run()