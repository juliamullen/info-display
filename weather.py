import requests
import json
import pytz

from datetime import datetime
from secret   import WEATHER_API_KEY

class Weather:
  def __init__(self):
    api_key = WEATHER_API_KEY
    city_id = "5125125"
    url     = f"https://api.openweathermap.org/data/2.5/forecast?units=imperial&id={city_id}&appid={api_key}"
    self.weather = self.get_weather()
    self.process_weather()

  def get_weather(self):
    # cache until application is live
    with open('weather.json', 'r') as rfile:
      weather = json.load(rfile)
    """
    weather = requests.get(url)
    with open('example.txt', 'w') as wfile:
      wfile.write(str(weather.json()))
    """
    return weather

  def process_weather(self):
    us_eastern = pytz.timezone('US/Eastern')
    self.frames = []

    for weather_frame in self.weather.get('list'):
      weather_utc_time = weather_frame.get('dt')
      weather_time = datetime.fromtimestamp(weather_utc_time, us_eastern)
      weather_temp = weather_frame.get('main').get('temp')
      weather_feels_like = weather_frame.get('main').get('feels_like')
      try:
        weather_desc =  weather_frame.get('weather')[0].get('description')
      except (IndexError, TypeError):
        weather_desc = None
      frame = {
          'time': weather_time,
          'temp': weather_temp,
          'feels_like': weather_feels_like,
          'desc': weather_desc
      }

      self.frames.append(frame)
