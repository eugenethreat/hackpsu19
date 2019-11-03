#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU
import requests
import json


from latLongGrabber import latLongGrabber
from latLongGrabber import stripper

addr = "New York City"

location = latLongGrabber(addr)

lat = location[0]
lng = location[1]


aw_geosite = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q='+location[0] + '%2C%20' + location[1]
response = requests.get("http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=jjK2n1LcGnGF7Nrouf8tD29fjVzyfxOM&q=40.7933949%2C-77.8600012")

f = response.json()
locKey = f["Key"]

aw_12hour = requests.get('http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/' +str(locKey) + '?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU')

g = aw_12hour.json()
weather_icon = []

#Weather_icon now contains all instances of weather_icon
for x in range(0,len(g)):
	weather_icon.append(g[x]["WeatherIcon"])

return weather_icon