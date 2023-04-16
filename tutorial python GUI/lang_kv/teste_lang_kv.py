import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    senha = ObjectProperty(None)
    
    # método press
    def press(self):
        username = self.name.text
        password = self.senha.text
        
        # if username != "" and not username.isspace():
        #     print(f'Usuario: {username}, Senha: {password}')
        #     self.add_widget(Label(text = f"Olá {username}"))
        # else: 
        #     print("Usuario vazio")
            
        print(f"O seu nome {username}, a senha {password}")

        #limpar o texto dos campos de input
        self.name.text = ""
        self.senha.text = ""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
    
if __name__ == "__main__":
    MyApp().run()