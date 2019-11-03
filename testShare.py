#GOOGLE API KEY - AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs
#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU

# DEPRECIATED - USE LATLONGGRABBER INSTEAD FOR CLARITY 

def stripper(location):
    location = location.replace('},',"")
    location = location.replace('{',"")
    location = location.replace(':',"")
    location = location.replace('\'',"")
    location = location.replace('lat',"")
    location = location.replace('lng',"")
    location = location.lstrip()
    location = location.rstrip()
    '''
    the output from mapped is formatted as a json ; this little bit of stuff takes that outputs and 
    formats it at "location, the element which comes before the lat/long
    '''
    return location

#actual program beginning ...
import googlemaps
from datetime import datetime

key = 'AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs'
gmaps = googlemaps.Client(key=key)

addr = 'State College, PA'
#40.78, -77.85 -- testing 

mapped = gmaps.geocode(addr)
strMapped=str(mapped) #converting to string to perform str operations 
latLongFromStrMapped = strMapped.rsplit("location")
location = str(latLongFromStrMapped[1])

location = stripper(location)
#location holds raw lat/lng vals 
#40.7933949,  -77.8600012 
#'location': {'lat': 40.7933949, 'lng': -77.8600012}, 

print(location) #for output purposes 


 

