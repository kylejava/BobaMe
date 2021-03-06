#BobaMe
#App began development in 5/22/2019


import kivy
import requests
import sys
import webbrowser
from pprint import pprint
import json
import random
import os
from kivy.base import runTouchApp
from func_app import locate , search_again 

from kivy.uix.floatlayout import FloatLayout
import urllib3
from time import sleep
from kivy.core.clipboard import Clipboard
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput

urllib3.disable_warnings()


class OpenScreen(Screen):
    user_location = ObjectProperty(0)
    def build(self):
        user_location = TextInput(multiline = False)
        self.user_location = user_location


class MainScreen(Screen):
    bobashop = ObjectProperty(0)
    bobalocation = ObjectProperty(0)
    bobaphone = ObjectProperty(0)
    bobareview = ObjectProperty(0)
    bobaimage = ObjectProperty("")
    current = ""
    def on_enter(self):
        user_city  = self.manager.get_screen("OpenScreen").user_location.text
        locate(self, user_city)
    def addSearch(self):
        user_city  = self.manager.get_screen("OpenScreen").user_location.text
        search_again(self , user_city)

    def directions(self):
        url = 'https://www.google.com/maps/place/'
        location = self.bobalocation.text
        webbrowser.open((url)+(location))



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("bobame.kv")
sm = WindowManager()
class BobaMeApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    BobaMeApp().run()
