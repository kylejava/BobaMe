import requests
import json
key = 'AIzaSyC0MF3ows--0wDHoelaabKb2fR8eE5qts0'
json = requests.get('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyC0MF3ows--0wDHoelaabKb2fR8eE5qts0').json()
print(json)
