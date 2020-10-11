import requests
from pprint import pprint

URL = "https://xkcd.com/info.0.json"

payload = {}

headers = {'Accept': 'application/json',}

response = requests.get(URL, headers=headers, data=payload)

sandwiches = response.json()

pprint(sandwiches)

pickles = sandwiches['safe_title']
tomato = sandwiches['num']
onion = sandwiches['img']

print(" ")
print("Today's XKCD comic is number " + str(tomato) + " called: " + str(pickles))
print("You can find it here: " + str(onion))