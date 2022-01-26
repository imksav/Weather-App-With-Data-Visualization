import database
import requests

cities = ['Ilam', 'Kathmandu', 'Ithari']

weather_dict = {}


def getWeatherData(city):
    response = requests.get(
        "http://api.weatherapi.com/v1/forecast.json?key=5728c4a08b1b4ea8b3695129221801&q="+city+"&days=7&aqi=yes&alerts=yes")
    # print(response)
    return response.json()


for city in cities:
    weather_dict[city] = getWeatherData(city)
    #storinng in variables
    location_name = (weather_dict[city]['location']['name'])
    location_lat = (weather_dict[city]['location']['lat'])
    location_lon = (weather_dict[city]['location']['lon'])
    # location_localtime=(weather_dict[city]['location']['localtime_epoch'])
    current_temperatue = (weather_dict[city]['current']['temp_c'])
    current_condition_location = (
        weather_dict[city]['current']['condition']['icon'])

    #inserting into database
    sql_query = "INSERT INTO general_info (location_name,location_lat,location_lon,current_location_temperature,current_location_conditon) VALUES (%s,%s,%s,%s,%s)"
    values = (location_name, location_lat, location_lon,
              current_temperatue, current_condition_location)

    # getting connection for database
    conn = database.connection()
    #inserting function calling
    database.insert_into_table(conn, sql_query, values)

    for i in range(3):
        #every day astro details
        date = (weather_dict[city]['forecast']
                ['forecastday'][i]['date'])
        #sunrise
        sunrise_time = (weather_dict[city]['forecast']
                        ['forecastday'][i]['astro']['sunrise'])

        #sunset
        sunset_time = (weather_dict[city]['forecast']
                       ['forecastday'][i]['astro']['sunset'])

        #moonrise
        moonrise_time = (weather_dict[city]['forecast']
                         ['forecastday'][i]['astro']['moonrise'])
        #moonset
        moonset_time = (weather_dict[city]['forecast']
                        ['forecastday'][i]['astro']['moonset'])

        #database
        sql_query = "INSERT INTO daily_forecast (date_list, location_name, sunrise_time, sunset_time, moonrise_time, moonset_time) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (date, location_name, sunrise_time,
                  sunset_time, moonrise_time, moonset_time)
        database.insert_into_table(conn, sql_query, values)
        for j in range(4):
            # every hour weather details
            #time
            hourly_time = (weather_dict[city]['forecast']
                           ['forecastday'][i]['hour'][j]['time'])
            #temp_c
            hourly_temp = (weather_dict[city]['forecast']
                           ['forecastday'][i]['hour'][j]['temp_c'])
            #condition in text
            hourly_temp_condition = (weather_dict[city]['forecast']['forecastday']
                                     [i]['hour'][j]['condition']['text'])
            #humidity
            hourly_humidity = (weather_dict[city]['forecast']
                               ['forecastday'][i]['hour'][j]['humidity'])
            #clouds
            hourly_cloud = (weather_dict[city]['forecast']
                            ['forecastday'][i]['hour'][j]['cloud'])
            #wind
            hourly_wind_kph = (weather_dict[city]['forecast']
                               ['forecastday'][i]['hour'][j]['wind_kph'])
            #is day or night
            isday = (weather_dict[city]['forecast']
                     ['forecastday'][i]['hour'][j]['is_day'])

            sql_query = "INSERT INTO hourly_forecast (location_name,date_list,hourly_time,hourly_temperature,hourly_temperature_condition,hourly_humidity,hourly_cloud,hourly_wind_kph,is_day) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (location_name, date, hourly_time, hourly_temp, hourly_temp_condition,
                      hourly_humidity, hourly_cloud, hourly_wind_kph, isday)
            database.insert_into_table(conn, sql_query, values)

# print(weather_dict["Butwal"])

    print(weather_dict[city]['location']['name'])
    print(weather_dict[city]['location']['lat'])
    print(weather_dict[city]['location']['lon'])
    print(weather_dict[city]['current']['temp_c'])
    print(weather_dict[city]['current']['condition']['icon'])
    for i in range(3):
        #every day
        print(weather_dict[city]['forecast']
              ['forecastday'][i]['date'])
        #every day astro details
        #sunrise
        print(weather_dict[city]['forecast']
              ['forecastday'][i]['astro']['sunrise'])

        #sunset
        print(weather_dict[city]['forecast']
              ['forecastday'][i]['astro']['sunset'])

        #moonrise
        print(weather_dict[city]['forecast']
              ['forecastday'][i]['astro']['moonrise'])
        #moonset
        print(weather_dict[city]['forecast']
              ['forecastday'][i]['astro']['moonset'])

        for j in range(4):
            # every hour weather details
            #time
            print(weather_dict[city]['forecast']
                  ['forecastday'][i]['hour'][j]['time'])
            #temp_c
            print(weather_dict[city]['forecast']
                  ['forecastday'][i]['hour'][j]['temp_c'])
            #condition in text
            print(weather_dict[city]['forecast']['forecastday']
                  [i]['hour'][j]['condition']['text'])
            #humidity
            print(weather_dict[city]['forecast']
                  ['forecastday'][i]['hour'][j]['humidity'])
            #clouds
            print(weather_dict[city]['forecast']
                  ['forecastday'][i]['hour'][j]['cloud'])
            #wind
            print(weather_dict[city]['forecast']
                  ['forecastday'][i]['hour'][j]['wind_kph'])
            print(weather_dict[city]['forecast']
                  ['forecastday'][i]['hour'][j]['is_day'])
            # print(weather_dict[city])
