from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Demo(GridLayout):
    pass

class TesteApp(App):
    def build(self):
        return Demo()
    
if __name__ == "__main__":
    TesteApp().run()