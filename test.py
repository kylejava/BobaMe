import requests
import json

def search(city , offset):
    PARAMETERS = {'term': 'boba',
                    'limit': 3,
                    'radius': 10000,
                    'location': city,
                    'offset': offset
                    }

    response = requests.get(url = ENDPOINT , params = PARAMETERS, headers = HEADERS)

    buisness_data = response.json()
    print(buisness_data)
    if ('error') in buisness_data:
        x = "Invalid"
        return (x)
    elif buisness_data['total'] == 0:
        x = "Invalid"
        return (x)
    else:
        for biz in buisness_data['businesses']:
            shop_name = (biz['name'])
            shop_location = ((str(biz['location']['address1'])) +(" ")+"\n"+ (str(biz['location']['city']))+ (" ") + (str(biz['location']['state']))+ (" ") + (str(biz['location']['zip_code'])))
            phone = (biz['phone'])
            review = ((str(biz['rating'])) + (" Stars"))
            image = (biz['image_url'])
            return [shop_name , shop_location , phone , review , image]


#API stuff
buisness_id = 'aAMbdEgSzj7k5UmGQu9fYg'
API_KEY = 'KyOYfJZS9HfNvVPmVD-QFj4ITXBV_ZAKLLjI2TxQHrlsGnfo0mVJJB8xtyV5BlW_p5-S_RmwhF8nrenZer_GC5lz6r9gZCM2pyi1rurotBNSebPFqOBQh_jvl4bLXHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}


#Main Function\
def main():
    print("Welcome to BobaMe!")
    print("")

    user_city = input("Enter your city or zip code to find the nearest boba shop: ")
    user_offset = 0

    shop = search(user_city , user_offset)
    while (shop == "Invalid"):
        user_city = input("Enter your city or zip code to find the nearest boba shop: ")
        user_offset = 0

        shop = search(user_city , user_offset)
        if (shop != "Invalid"):
            break
        else:
            pass
    print(shop)
    print("")
#    try_again = input("Would you like to find more options? y/n ")

#    while(try_again == "y" or try_again == "Y"):
#        while(user_offset != 6):
#            user_offset = user_offset + 3
#            search(user_city , user_offset)
#            print("")
#            if(user_offset == 6):
#                break
#            else:
#                try_again = input("Would you like to find more options? y/n ")
#        break



main()
