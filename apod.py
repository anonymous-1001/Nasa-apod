import requests
import json
import webbrowser

api_key = "kBUtp4YTwFGP56Y7A1LihpAXUwaI4hTvDsGCwWJ0"
api_url="https://api.nasa.gov/planetary/apod"

#date = input("Enter date to for astronomy picture of the day (YYYY-MM-DD)>>>")

params = {
    "date": "2023-11-09",
    "hd": True,
    "api_key":api_key
}
response = requests.get(api_url,params=params)
json_data = json.loads(response.text)
image_url = json_data['hdurl']
webbrowser.open(image_url)