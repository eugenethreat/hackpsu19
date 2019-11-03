#GOOGLE API KEY - AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs
#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU

#USE THIS FILE 

global location

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
'''
def latLongGrabber():
    import googlemaps
    from datetime import datetime

    key = 'AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs'
    gmaps = googlemaps.Client(key=key)

    addr = 'San Fransisco, CA'
    #40.78, -77.85 -- testing 

    mapped = gmaps.geocode(addr)
    strMapped=str(mapped) #converting to string to perform str operations 
    latLongFromStrMapped = strMapped.rsplit("location")
    location = str(latLongFromStrMapped[1])

    location = stripper(location)
    location = location.split(',')
    #location holds raw lat/lng vals, as a list 
    #[40.7933949],[-77.8600012] 
    #'location': {'lat': 40.7933949, 'lng': -77.8600012}, 
    #return location
    print('lat: ',location[0],'lng: ',location[1]) #for output purposes 
    return location
'''

def latLongGrabber(addr):
    #version that takes a passed argument 
    import googlemaps
    from datetime import datetime

    key = 'AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs'
    gmaps = googlemaps.Client(key=key)

    mapped = gmaps.geocode(addr)
    strMapped=str(mapped) #converting to string to perform str operations 
    latLongFromStrMapped = strMapped.rsplit("location")
    location = str(latLongFromStrMapped[1])

    location = stripper(location)
    location = location.split(',')

    #location holds raw lat/lng vals, as a list 
    #[40.7933949],[-77.8600012] 
    #'location': {'lat': 40.7933949, 'lng': -77.8600012}, 
    #return location

    return location
