#ACCUWEATHER API KEY - EjXAs6PEgwDxzY8dVLplxpEvOfTu8lAZ

#Import Requests Library for getting AccuWeather API data
import requests
#Import JSON Library for parsing the AccuWeather API data
import json

def weather(addr):

	location = addr

	'''
		Define Latitude and Longitude, and send them into the Accuweather Location API.
		This returns a location key value.
	'''
	lat = location['lat']
	lng = location['lng']


	aw_geosite = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=EjXAs6PEgwDxzY8dVLplxpEvOfTu8lAZ&q='+ str(lat) + '%2C%20' + str(lng)
	response = requests.get(aw_geosite)

	f = response.json()
	locKey = f["Key"]
	'''
		Takes the Location Key value and sends it through the Accuweather 12-Hour Forecast API,
		assigning g to be the API output in .json format
	'''

	aw_12hour = requests.get('http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/' +str(locKey) + '?apikey=EjXAs6PEgwDxzY8dVLplxpEvOfTu8lAZ')

	g = aw_12hour.json()
	weather_icon = []

	'''
		We iterate over a range from 0 to len(g) where we gather
		the weather_icons from every hour and input them into a list
		from hour 0 to hour 11.
	'''
	for x in range(0,len(g)):
		weather_icon.append(g[x]["WeatherIcon"])

	return weather_icon