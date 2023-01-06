import kivy
kivy.require("1.0.9")
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

Builder.load_string("cols: 1 Label: text: ola")

class Main:
    print("ola")
