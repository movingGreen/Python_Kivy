from kivy.app import App
from kivy.garden.mapview import MapMarkerPopup

class MainApp(App):
    latitude = -25
    longitude = -25
    
    def on_start(self):
        marker = MapMarkerPopup(lat = self.latitude, lon = self.longitude)
        self.root.lat = self.latitude
        self.root.lon = self.longitude
        self.root.add_widget(marker)
    pass

MainApp().run()