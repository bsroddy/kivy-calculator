import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'width', '110')
Config.set('graphics', 'height', '150')


class ButtonPad(Widget):
    """The buttons of the calculator. Contains digits 0-9, the four arithmetic operations,
     the clear button, and the equals button."""
    pass

class Screen(Widget):
    """The area of the calculator that will display the numbers the user enters and processes."""
    pass

class Calculator(Widget):
    """The widget that combines the Screen and ButtonPad."""
    pass

class CalculatorApp(App):
    """The main app."""
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()

