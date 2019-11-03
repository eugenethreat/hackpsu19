#GOOGLE API KEY - AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs
#ACCUWEATHER API KEY - 5u1ZRpMU9yQ2urfUL5cU1a3N2fFw3zAU

#USE THIS FILE 

global location

import json
import googlemaps
import pprint
import requests
from datetime import datetime

'''
this file takes an origin and destination as parameters, then 
returns a nested list of the lat/long values, and the duration 
of each step. 

'''
def directinonalReturn(origin, destination):
    key = 'AIzaSyBjkt7bJVDGfg0eInZv4lTOMx6NCxTBVgs'
    gmaps = googlemaps.Client(key=key)

    orig = "State"+"College"+"PA"
    dest = "New"+"York"+"City"+"NY"

    #mapped = gmaps.directions(orig, dest) shit library

    '''https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=YOUR_API_KEY'''

    route = 'https://maps.googleapis.com/maps/api/directions/json?origin='+ orig +'&destination=' + dest + '&key=' + key
    response = requests.get(route)
        #raw API call

    '''the route info is contained in the param 'legs' ''' 
    routeAsJson = response.json() #a dictionary of key 

    #print(routeAsJson['routes'])
    jsonAsDict = jsonToObject(routeAsJson)
    coordsAndDuration = legsToDict(jsonAsDict)

    print(coordsAndDuration)


def jsonToObject(passedJson):
    jsonToStr = json.dumps(passedJson)
    jsonAsDict = json.loads(jsonToStr)
    #print(type(jsonToStr))
    #print(type(jsonAsDict))

    return jsonAsDict

def legsToDict(passedDict):
    #print(passedDict['routes'][0]['legs'][0]['distance']) 
        #access the lat and long of the first value 
    
    stepList = []
    length_key = len(passedDict['routes'][0]['legs'][0]['steps'])  # length of the list stored at `'key'` ...
    length_key = length_key 
    #print("lk: ",length_key)

    for x in range(length_key):
        leg1 = passedDict['routes'][0]['legs'][0]['steps'][x]
        duration = passedDict['routes'][0]['legs'][0]['steps'][x]['duration']
        endLoc = passedDict['routes'][0]['legs'][0]['steps'][x]['end_location']
        
        valuesToAdd = [endLoc, duration]

        ''' 
        21 ayaya:  {'distance': 
            {'text': '197 ft', 'value': 60}, 
            'duration': {'text': '1 min', 'value': 19}, 
            'end_location': {'lat': 40.7124773, 'lng': -74.0062007}, 
            'html_instructions': 'Turn <b>right</b> onto <b>Steve Flanders Square</b><div style="font-size:0.9em">Restricted usage road</div>', 
            'maneuver': 'turn-right', 
            'polyline': {'points': 'yqnwFrfubMWLA?C@A@A@?@A?[bAEH'}, 
            'start_location': {'lat': 40.7121262, 'lng': -74.0056991}, '
             travel_mode': 'DRIVING'}
        '''
        stepList.append(valuesToAdd)

        print("returned, done") 
        return stepList

#aaa
directinonalReturn("State College, PA", "New York City, NY")
  