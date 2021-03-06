import requests
import webbrowser
import json
from keys import *
from plyer import gps
from plyer.facades import GPS
from kivy.clock import Clock, mainthread
import ssl
ssl.match_hostname = lambda cert, hostname: True


def search(city , offset):
    buisness_id = 'Insert Buisness ID'
    API_KEY = getAPIKey()
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
    print(buisness_data)
    if('error') in buisness_data:
        x = "Invalid"
        return (x)
    elif not buisness_data['businesses']:
        x = "None"
        return (x)
    for biz in buisness_data['businesses']:
        shop_name = (biz['name'])
        shop_location = ((str(biz['location']['address1'])) +(" ")+"\n "+ (str(biz['location']['city']))+ (" ") + (str(biz['location']['state']))+ (" ") + (str(biz['location']['zip_code'])))
        phone = (biz['display_phone'])
        review = ((str(biz['rating']) + (" Stars")))
        image = (biz['image_url'])
        return [shop_name , shop_location , phone , review , image]



def locate(self , user_city):
    #key = getAPI_g()
    #send_url = ("http://api.ipstack.com/check?access_key="+str(key))
    #geo_req = requests.get(send_url)
    #geo_json = json.loads(geo_req.text)
    #user_city = geo_json['zip']



    offset = 0
    self.offset = 0
    shop = search(user_city , offset)
    if(shop == "Invalid"):
        print("Go Back and input again")
        offset = 0
        self.offset = 0
        shop = search(user_city , offset)
        if(shop == "Invalid"):
            self.manager.current = 'OpenScreen'
            self.manager.transition.direction = "right"


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



def search_again(self, user_city):
    self.bobareview.text = " "
    if(self.offset < 7):
        self.offset += 1
        self.shop = search(user_city , (self.offset))
    #    if(self.shop == "Invalid"):
    #        print("Go Back and input again")
    #        self.shop = search(user_city , (self.offset))
    #    if(self.shop == "None"):
    #        print("No More Boba Shops To Preview, Going Back to Homescreen")
    #        self.manager.current = 'OpenScreen'
    #        self.manager.transition.direction = "right"
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
        print(shop_review)
        self.bobaimage = shop_image
        print(self.offset)
    elif(self.offset >= 7):
        print(self.offset)
