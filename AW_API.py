#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU

#Import Requests Library for getting AccuWeather API data
import requests
#Import JSON Library for parsing the AccuWeather API data
import json

#Testing check
#addr = "Tampa, Florida"

def weather(addr):

	location = addr

	'''
		Define Latitude and Longitude, and send them into the Accuweather Location API.
		This returns a location key value.
	'''
	lat = location['lat']
	lng = location['lng']


	aw_geosite = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q='+ str(lat) + '%2C%20' + str(lng)
	response = requests.get(aw_geosite)

	f = response.json()
	locKey = f["Key"]
	'''
		Takes the Location Key value and sends it through the Accuweather 12-Hour Forecast API,
		assigning g to be the API output in .json format
	'''

	aw_12hour = requests.get('http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/' +str(locKey) + '?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU')

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