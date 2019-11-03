#########################################################
#grouping fuction to decide severity of weather
#
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
            15:4,
            16:3,
            17:3,
            18:3,
            19:3,
            20:3,
            21:3,
            22:4,
            23:4,
            24:6,
            25:6,
            26:6,
            29:5,
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
            40:3,
            41:5,
            42:5,
            43:4,
            44:5}


            

def severity(weatherVal=[]):
    severityList = []
    for key in weatherVal:
        try:
            val = severDict[key]
            severityList.append(val)
        except KeyError as e:
            severityList.append(0)

    return(severityList)

