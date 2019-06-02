import kivy
import requests
import sys
from pprint import pprint
import json
import random

from get_a import getAPI
from func_app import locate , search_again , go_back

import urllib3
from time import sleep
import codecs
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
urllib3.disable_warnings()

def search(city , offset):
    buisness_id = 'aAMbdEgSzj7k5UmGQu9fYg'
    API_KEY = getAPI()
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'Bearer %s' % API_KEY}
    PARAMETERS = {'term': 'boba',
                    'limit': 1,
                    'radius': 10000,
                    'location': city,
                    'offset': offset
                    }
    response = requests.get(url = ENDPOINT , params = PARAMETERS, headers = HEADERS)
    buisness_data = response.json()

    for biz in buisness_data['businesses']:
        shop_name = (biz['name'])
        shop_location = ((str(biz['location']['address1'])) +(" ")+"\n"+ (str(biz['location']['city']))+ (" ") + (str(biz['location']['state']))+ (" ") + (str(biz['location']['zip_code'])))
        phone = (biz['phone'])
        review = ((str(biz['rating'])) + (" Stars"))
        image = (biz['image_url'])
        return [shop_name , shop_location , phone , review , image]



class OpenScreen(Screen):
    pass

class MainScreen(Screen):
    bobashop = ObjectProperty(0)
    bobalocation = ObjectProperty(0)
    bobaphone = ObjectProperty(0)
    bobareview = ObjectProperty(0)
    bobaimage = ObjectProperty(" ")
    current = ""
    def on_enter(self):
        locate(self)
    def addSearch(self):
        search_again(self)
    def subSearch(self):
        go_back(self)



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("bobame.kv")
sm = WindowManager()
class BobaMeApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    BobaMeApp().run()
