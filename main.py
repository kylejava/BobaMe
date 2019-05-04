
#api key
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

    for biz in buisness_data['businesses']:
        print(biz['name'])
        print((str(biz['location']['address1'])) +(" ")+ (str(biz['location']['city']))+ (" ")+ (str(biz['location']['state']))+ (" ") + (str(biz['location']['zip_code'])))
        print(biz['phone'])
        print((str(biz['rating'])) + (" Stars"))
        print()

#API stuff
buisness_id = 'aAMbdEgSzj7k5UmGQu9fYg'
API_KEY = 'YOUR API KEY'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}


#Main Function\
def main():
    print("Welcome to BobaMe!")
    print("")

    user_city = input("Enter your city or zip code to find the nearest boba shop: ")
    user_offset = 0

    search(user_city , user_offset)
    print("")
    try_again = input("Would you like to find more options? y/n ")

    while(try_again == "y" or try_again == "Y"):
        while(user_offset != 6):
            user_offset = user_offset + 3
            search(user_city , user_offset)
            print("")
            if(user_offset == 6):
                break
            else:
                try_again = input("Would you like to find more options? y/n ")
        break



main()
