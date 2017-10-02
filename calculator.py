import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class ButtonPad(Widget):
    """The buttons of the calculator. Contains digits 0-9, the four arithmetic operations,
     the clear button, and the equals button."""
    pass


class CalculatorApp(App):
    """The main app."""
    def build(self):
        """Currently only displays the numpad."""
        return ButtonPad()

if __name__ == '__main__':
    CalculatorApp().run()

