import kivy
import requests
import sys
from pprint import pprint
import json
import random
from get_a import getAPI
import func_app
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
        #url = 'https://ipinfo.io/'
        #res = requests.get(url, auth=('user' , 'pass') , verify=False)
        #data = res.json()
        send_url = "http://api.ipstack.com/check?access_key=f787f7960a63899a81ebae839b4f4903"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        user_city = geo_json['zip']

        #user_city = data['postal']
        offset = 0
        self.offset = 0
        shop = search(user_city , offset)
        self.shop = shop
        shop_name = shop[0]
        shop_location = shop[1]
        shop_phone = shop[2]
        shop_review = shop[3]
        shop_image = shop[4]
        self.bobashop.text = shop_name
        self.bobalocation.text = shop_location
        self.bobaphone.text = shop_phone
        self.bobareview.text = shop_review
        print(self.offset)
        self.bobaimage = shop_image

    def addSearch(self):
        if(self.offset < 7):
            #res = requests.get('https://ipinfo.io/')
            #data = res.json()
            #user_city = data['postal']
            send_url = "http://api.ipstack.com/check?access_key=f787f7960a63899a81ebae839b4f4903"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            user_city = geo_json['zip']

            self.offset += 1
            self.shop = search(user_city , (self.offset))
            shop = self.shop
            shop_name = shop[0]
            shop_location = shop[1]
            shop_phone = shop[2]
            shop_review = shop[3]
            shop_image = shop[4]
            self.bobashop.text = shop_name
            self.bobalocation.text = shop_location
            self.bobaphone.text = shop_phone
            self.bobareview.text = shop_review
            self.bobaimage = shop_image
            print(self.offset)
        elif(self.offset >= 7):
            print(self.offset)


    def subSearch(self):
        if(self.offset > 0):
            #res = requests.get('https://ipinfo.io/')
            #data = res.json()
            #user_city = data['postal']
            send_url = "http://api.ipstack.com/check?access_key=f787f7960a63899a81ebae839b4f4903"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            user_city = geo_json['zip']
            self.offset = self.offset - 1
            self.shop = search(user_city , (self.offset))
            shop = self.shop
            shop_name = shop[0]
            shop_location = shop[1]
            shop_phone = shop[2]
            shop_review = shop[3]
            shop_image = shop[4]
            self.bobashop.text = shop_name
            self.bobalocation.text = shop_location
            self.bobaphone.text = shop_phone
            self.bobareview.text = shop_review
            print(self.offset)
            self.bobaimage = shop_image
        elif(self.offset == 0):
            print(self.offset)




class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("bobame.kv")
sm = WindowManager()
class BobaMeApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    BobaMeApp().run()
