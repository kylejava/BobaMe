import requests
import json
from get_a import getAPI_g , getAPI_y
from plyer import gps
from test import get_loc

def search(city , offset):
    buisness_id = 'aAMbdEgSzj7k5UmGQu9fYg'
    API_KEY = getAPI_y()
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

def locate(self):
    #key = getAPI_g()
    #send_url = ("http://api.ipstack.com/check?access_key="+str(key))
    #geo_req = requests.get(send_url)
    #geo_json = json.loads(geo_req.text)
    #user_city = geo_json['zip']
    user_city = get_loc()
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
    def change_image(self , shop_image):
        self.bobaimage = shop_image


def search_again(self):
    if(self.offset < 7):
        url = requests.get('https://geoipify.whoisxmlapi.com/api/v1?apiKey=at_JJ2zyiDJqOnVLxqEaHVKfTggXeJm0')
        json = json.loads(url.text)
        user_city = (json['location']['postalCode'])
        self.offset += 1
        self.shop =search(user_city , (self.offset))
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

def go_back(self):
    if(self.offset > 0):
        #key = getAPI_g()
        #send_url = ("http://api.ipstack.com/check?access_key="+str(key))
        #geo_req = requests.get(send_url)
        #geo_json = json.loads(geo_req.text)
        #latitude = geo_json['latitude']
        #longitude = geo_json['longitude']
        #user_city = geo_json['zip']
        url = requests.get('https://geoipify.whoisxmlapi.com/api/v1?apiKey=at_JJ2zyiDJqOnVLxqEaHVKfTggXeJm0')
        json = json.loads(url.text)
        user_city = (json['location']['postalCode'])
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
        self.bobareview = shop_review
        print(self.offset)
        self.bobaimage = shop_image
    elif(self.offset == 0):
        print(self.offset)
