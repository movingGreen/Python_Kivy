import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
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
        self.top_grid.cols = 2
        
        # adicionar widgets 
        self.top_grid.add_widget(Label(
            text = "Usuario: ",
            font_size = 32,
            ))
        
        # adicionar Input Box
        self.name = TextInput(
            multiline = False,
            font_size = 32,
            )
        self.top_grid.add_widget(self.name)
        
        self.top_grid.add_widget(Label(
            text = "Senha: ",
            font_size = 32,
            ))
        # adicionar Input Box
        self.senha = TextInput(
            multiline = False,
            font_size = 32,  
            )
        self.top_grid.add_widget(self.senha)
        
        # adicionar o top_grid no app
        self.add_widget(self.top_grid)
        
        # adicionar um submit botão
        self.submit = Button(text = "LOGIN",
                             font_size = 32,
                             size_hint_y = None,
                             height = 50
                             )
        self.submit.bind(on_press = self.press)
        
        self.add_widget(self.submit)
        
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