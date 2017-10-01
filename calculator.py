import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Numpad(Widget):
    """The numpad, digits 0-9. No other buttons."""
    pass


class CalculatorApp(App):
    """The main app."""
    def build(self):
        """Currently only displays the numpad."""
        return Numpad()

if __name__ == '__main__':
    CalculatorApp().run()

