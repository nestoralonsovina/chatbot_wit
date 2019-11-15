import cleverbotfree.cbfree
from wit import Wit
from datetime import datetime
import requests
import json

credentials = None

with open("credentials.json", "r") as fd:
    content = fd.read()
    credentials = json.loads(content)

class Bot:

    access_token = credentials['credentials']['wit_access_token']
    weather_token = credentials['credentials']['openweather_access_token']

    @staticmethod
    def generate_response(message):
        return {"response": message}

    def __init__(self):
        self.client = Wit(self.access_token)
        self.cb = cleverbotfree.cbfree.Cleverbot()

    def request(self, message):
        self.request_message = message
        answer = self.client.message(message)
        self.r = answer

    def response(self):
        if len(self.r['entities']) == 0 or "intent" not in self.r['entities']:
            return self.chat()
        if self.r['entities']['intent'][0]['confidence'] < 0.8:
            return self.chat()
        if self.r['entities']['intent'][0]['value'] == "greetings":
            return self.chat()
        if self.r['entities']['intent'][0]['value'] == "get_temperature":
            return self.get_weather()
        if self.r['entities']['intent'][0]['value'] == "get_hour":
            return self.get_hour()

    def chat(self):
        response = self.cb.single_exchange(self.request_message)
        return self.generate_response(response)

    def get_weather(self):
        coords = [48, 2]
        if "location" in self.r['entities']:
            coords = [self.r['entities']['location'][0]['resolved']['values'][0]['coords']['lat'],
                      self.r['entities']['location'][0]['resolved']['values'][0]['coords']['long']]
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&APPID={self.weather_token}")
        weather = json.loads(weather.content)
        convert = lambda t: (t - 273.15)
        return self.generate_response(f"{convert(weather['main']['temp']):.2f} degrees")

    def get_hour(self):
        return self.generate_response("The current time is: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
