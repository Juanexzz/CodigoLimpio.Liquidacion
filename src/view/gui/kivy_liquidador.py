import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Main_screen import MainScreen
from Second_screen import SecondScreen

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
        

class liquidadorLaboral(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(SecondScreen(name = "second"))
        return sm

if __name__ == "__main__":
    liquidadorLaboral().run()


#Ver porque no me esta borrando los datos con el boton volver