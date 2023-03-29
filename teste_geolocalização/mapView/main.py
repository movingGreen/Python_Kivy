from kivy.app import App
from kivy.garden.mapview import MapMarkerPopup

class MainApp(App):
   
    
    def build(self):
        latitude = 25
        longitude = 25
        marker = MapMarkerPopup(lat = latitude, lon = longitude)
        # self.root.lat = latitude
        # self.root.lon = longitude
        self.root.add_widget(marker)
        pass
    

MainApp().run()