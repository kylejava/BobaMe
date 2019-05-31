import requests
import json
from get_a import getAPI
class function():
    buisness_id = 'aAMbdEgSzj7k5UmGQu9fYg'
    API_KEY = getAPI()
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'Bearer %s' % API_KEY}

    def search(city , offset):
        PARAMETERS = {'term': 'boba',
                        'limit': 1,
                        'radius': 10000,
                        'location': city,
                        'offset': offset
                        }

        response = requests.get(url = function.ENDPOINT , params = PARAMETERS, headers = function.HEADERS)

        buisness_data = response.json()

        for biz in buisness_data['businesses']:
            shop_name = (biz['name'])
            shop_location = ((str(biz['location']['address1'])) +(" ")+"\n"+ (str(biz['location']['city']))+ (" ") + (str(biz['location']['state']))+ (" ") + (str(biz['location']['zip_code'])))
            phone = (biz['phone'])
            review = ((str(biz['rating'])) + (" Stars"))
            image = (biz['image_url'])
            return [shop_name , shop_location , phone , review , image]

    def locate(self):
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        user_city = data['postal']
        offset = 0
        self.offset = 0
        shop = function.search(user_city , offset)
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


    def search_again(self):
        if(self.offset < 7):
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            user_city = data['postal']
            self.offset += 1
            self.shop = function.search(user_city , (self.offset))
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
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            user_city = data['postal']
            self.offset = self.offset - 1
            self.shop = function.search(user_city , (self.offset))
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