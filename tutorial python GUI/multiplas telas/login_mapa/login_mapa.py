from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView

class LoginTela(Screen):
    pass

class MapaTela(Screen):
    
    pass

class GerenciadorTelas(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_file("layout_login.kv")
    
if __name__ == "__main__":
    MyApp().run()