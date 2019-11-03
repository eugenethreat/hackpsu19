#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU
import requests

import latLongGrabber
x= latLongGrabber.latLongGrabber()
print(x)

API_Key = 'u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU'
aw_geosite = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q='+str(latLongGrabber.location[0]) + '%2C%20' +str(latLongGrabber.location[1])
response = requests.get("http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU&q=40.78%2C%20-77.85")

print(response)

#Run location key through forecast
