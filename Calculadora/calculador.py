import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.cols = 4

        self.add_widget(Button(text="7"))
        self.add_widget(Button(text="8"))
        self.add_widget(Button(text="9"))
        self.add_widget(Button(text="/"))

        self.add_widget(Button(text="4"))
        self.add_widget(Button(text="5"))
        self.add_widget(Button(text="6"))
        self.add_widget(Button(text="*"))

        self.add_widget(Button(text="1"))
        self.add_widget(Button(text="2"))
        self.add_widget(Button(text="3"))
        self.add_widget(Button(text="-"))

        self.add_widget(Button(text="0"))
        self.add_widget(Button(text="."))
        self.add_widget(Button(text="="))
        self.add_widget(Button(text="+"))

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()