#importing the requests module to allow sending of HTTP requests
import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=4b84c48893285fb922690f8ae9d5e5b5&units=metric&q='

print('Weathex Description')
while True:
    city = input('Search for a city..\n')
    if city == 'q' or 'Q':
        break
    #concatinating the base_url and city input to complete the query from user
    try:
        url = base_url + city

        json_data = requests.get(url).json()
        weather_description = json_data['weather'][0]['description']
        country = json_data['sys']['country']
        temp = json_data['main']['temp']
        print('Country:',country)
        print('Temperature:',temp)
        print(weather_description)
    except:
        #Display error when city name is invalid or no internet connection is available
        print('Invalid city name!\nOr\nNo internet connection')

quit = input('press any key to close application')
