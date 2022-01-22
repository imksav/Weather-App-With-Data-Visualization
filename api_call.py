import requests
import credentials
# response = requests.get('https://github.com/timeline.json')
# print(response.json)
# if response:
#      print("Connection status is success. Status code::", response.status_code)
# else:
#      print("Connection status is not success, Status code::", response.status_code)

cities = ['Butwal', 'Kathmandu', 'Pokhara']
weather_dict = {}
def getWeatherData(city):
     response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid="+credentials.APP_ID+"&q="+city+"")
     print(response)
     return response.json()
     
for city in cities:
     weather_dict[city] = getWeatherData(city)
     print(weather_dict[city])
     
     