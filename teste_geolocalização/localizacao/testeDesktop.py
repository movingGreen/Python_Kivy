from kivy.app import App
from kivy.uix.label import Label
from geopy.geocoders import Nominatim


class MyApp(App):
    def build(self):
        label = Label(text = self.get_location())
        return label
    
    def get_location(self):
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode("my_location")
        latitude = location.latitude
        longitude = location.longitude

        return f"Latitude: {latitude}\nLongitude: {longitude}"
    
if __name__ == "__main__":
    MyApp().run()