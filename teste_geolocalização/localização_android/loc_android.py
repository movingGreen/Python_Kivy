import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from android.permissions import request_permissions, Permission
from android import AndroidService
from plyer import gps


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        # Solicitar permissões para acessar a localização do dispositivo
        request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION])

        # Iniciar o serviço de GPS
        service = AndroidService('gps', 'gps', 'location')
        service.start()

        # Obter a localização atual do dispositivo
        location = gps.get_location()

        # Exibir a localização no console
        print(f"Latitude: {location['lat']}, Longitude: {location['lon']}")


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()
