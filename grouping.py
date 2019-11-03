#########################################################
# grouping fuction to decide severity of weather
#
#########################################################

#########################################################
#https://developer.accuweather.com/weather-icons
#1 = clear, good travel
#2 = overcast still good
#3 = fog, rain with sun
#5 = thunderstorm,heavy rain,
#7 = rain/snow, bad rain at night
#10 = ice, terrible
#########################################################
severDict = {1:1,
            2:1,
            3:1,
            4:1,
            5:1,
            6:1,
            7:2,
            8:2,
            11:3,
            12:3,
            13:2,
            14:2,
            15:5,
            16:3,
            17:3,
            18:3,
            19:3,
            20:3,
            21:3,
            22:5,
            23:5,
            24:10,
            25:10,
            26:10,
            29:7,
            30:2,
            31:2,
            32:2,
            33:1,
            34:1,
            35:1,
            36:1,
            37:1,
            38:2,
            39:2,
            40:5,
            41:7,
            42:7,
            43:5,
            44:7}



def severity(weatherVal=[]):
    severityList = []
    for key in weatherVal:
        try:
            val = severDict[key]
            severityList.append(val)
        except KeyError as e:
            severityList.append(0)

    return(severityList)

