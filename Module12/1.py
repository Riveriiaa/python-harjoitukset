import json
from urllib.request import Request, urlopen

url = "https://api.chucknorris.io/jokes/random"

request = Request(
    url,
    headers={"User-Agent": "Markus"}
)

with urlopen(request) as response:
    data = json.load(response)

print(data["value"])