from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#definir as telas diferentes
class PrimeiraTela(Screen):
    pass

class SegundaTela(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("layout_nova_tela.kv")


class AwesomeApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    AwesomeApp().run()