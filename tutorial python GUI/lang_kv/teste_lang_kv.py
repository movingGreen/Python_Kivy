import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGridLayout(Widget):
    # inicializar a palavra chave infinite
    def __init__(self, **kwargs):
        # Chamar o construtor do grid layout
        super(MyGridLayout, self).__init__(**kwargs)

        # crie as colunas
        self.cols = 1
        self.row_force_default = True
        self.col_force_default = True
        self.row_default_height = 120
        self.col_default_width = 400
        
        # criar um segundo gridlayout
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height = 40,
            col_force_default = True,
            col_default_width = 400
        )
     
    # método press
    def press(self, instance):
        username = self.name.text
        password = self.senha.text
        
        if username != "" and not username.isspace():
            print(f'Usuario: {username}, Senha: {password}')
            self.add_widget(Label(text = f"Olá {username}"))
        else: 
            print("Usuario vazio")
            
        #limpar o texto dos campos de input
        self.name.text = ""
        self.senha.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
    
if __name__ == "__main__":
    MyApp().run()