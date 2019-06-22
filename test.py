import requests

params = {"api-key": 'a68a9652ad250438b0dba34249662d66ca13cdde549431e6da0c5798'}
json = requests.get('https://api.ipdata.co', params=params).json()
print(json['postal'])
