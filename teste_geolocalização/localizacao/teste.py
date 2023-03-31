from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from geopy.geocoders import Nominatim
from jnius import autoclass

class MyApp(App):
    def build(self):
        label = Label(text=self.get_location())
        return label

    def get_location(self):
        # Check if running on Android
        if platform == 'android':
            
            # Access the Android location service
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            locationManager = mActivity.getSystemService(Context.LOCATION_SERVICE)
            
            # Check if location permission is granted
            if ActivityCompat.checkSelfPermission(mActivity, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED:
                location = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER)
                latitude = location.getLatitude()
                longitude = location.getLongitude()
            else:
                latitude = "Location permission not granted"
                longitude = "Location permission not granted"
        else:
            # Retrieve the user's geolocation using geopy
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode("my_location")
            latitude = location.latitude
            longitude = location.longitude

        return f"Latitude: {latitude}\nLongitude: {longitude}"

if __name__ == '__main__':
    MyApp().run()
