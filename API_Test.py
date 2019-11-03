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

API_Key = 'jjK2n1LcGnGF7Nrouf8tD29fjVzyfxOM'
aw_geosite = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q='+location[0] + '%2C%20' + location[1]
response = requests.get("http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=jjK2n1LcGnGF7Nrouf8tD29fjVzyfxOM&q=40.7933949%2C-77.8600012")

print(response.json())

#Run location key through forecast
