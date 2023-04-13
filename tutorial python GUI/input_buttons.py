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
        
        # adicionar widgets 
        self.add_widget(Label(text = "Usuario: "))
        
        # adicionar Input Box
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text = "Senha: "))
        # adicionar Input Box
        self.pizza = TextInput(multiline = False)
        self.add_widget(self.pizza)
        
        # adicionar um submit botão
        self.submit = Button(text = "Submit", font_size = 25)
        self.add_widget(self.submit)

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
    
if __name__ == "__main__":
    MyApp().run()