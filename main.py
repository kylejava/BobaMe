import kivy
import requests
import json
import random
import urllib.request
from get_a import getAPI
import func_app
from func_app import function
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput




class OpenScreen(Screen):
    pass

class MainScreen(Screen):
    bobashop = ObjectProperty(0)
    bobalocation = ObjectProperty(0)
    bobaphone = ObjectProperty(0)
    bobareview = ObjectProperty(0)
    bobaimage = ObjectProperty(" ")
    current = ""
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.user_city = ""
    def on_enter(self):
        function.locate(self)

    def addSearch(self):
        function.search_again(self)

    def subSearch(self):
        function.go_back(self)



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("bobame.kv")

class BobaMeApp(App):
    def build(self):
        return kv
if __name__ =="__main__":
    BobaMeApp().run()
