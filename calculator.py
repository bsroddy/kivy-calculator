import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config


class ButtonPad(Widget):
    """The buttons of the calculator. Contains digits 0-9, the four arithmetic operations,
     the clear button, and the equals button."""
    pass

class Screen(Widget):
    """The area of the calculator that will display the numbers the user enters and processes."""
    def get_screen_text(self):
        return self.ids['screen_text'].text

    def set_screen_text(self, new_text):
        self.ids['screen_text'].text = new_text

    def clear_screen_text(self):
        self.ids['screen_text'].text = ''

    def add_digit_to_screen(self, digit):
        current_screen_text = self.get_screen_text()
        self.set_screen_text(current_screen_text + digit)

    def enter_button(self, button_entry):
        if len(button_entry) == 1:
            if button_entry.isdigit():
                self.add_digit_to_screen(button_entry)

class Calculator(Widget):
    """The widget that combines the Screen and ButtonPad."""
    pass

class CalculatorApp(App):
    """The main app."""
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()

