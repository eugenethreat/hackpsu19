#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU
import requests


from latLongGrabber import latLongGrabber
from latLongGrabber import stripper

addr = "New York City"

location = latLongGrabber(addr)

lat = location[0]
lng = location[1]

'''
print("lat: ", lat)
print("long: ", lng)
'''

API_Key = 'u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU'
aw_geosite = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q='+location[0] + '%2C%20' + location[1]
response = requests.get("http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q=40.78%2C%20-77.85")

print(response)

#Run location key through forecast
