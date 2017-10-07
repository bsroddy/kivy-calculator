import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config

class Calculator(BoxLayout):
    """The widget that combines the Screen and ButtonPad."""

    def get_screen_text(self):
        return self.ids["screen"].text

    def set_screen_text(self, new_text):
        self.ids['screen'].text = new_text

    def clear_screen_text(self):
        self.ids['screen'].text = ''

    def add_digit_to_screen(self, digit):
        current_screen_text = self.get_screen_text()
        self.set_screen_text(current_screen_text + digit)

    def enter_button(self, button_entry):
        if len(button_entry) == 1:
            if button_entry.isdigit():
                self.add_digit_to_screen(button_entry)

            if button_entry == 'C':
                self.clear_screen_text()


class CalculatorApp(App):
    """The main app."""
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()

