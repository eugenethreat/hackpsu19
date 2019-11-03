'''
    Taking in the weather values for every specific point we defined,
    we check it against out predefined dictionary of severities in
    grouping.py, and will suggest a preferred starting time based on
    average weather severity along the path.
'''

def weight(bigList,waitTime=3):

    bigListWeights = []

    for c in range(waitTime+1):
        totalTime = 0
        currentSeverity = 0

        for pathServ in bigList:
            time = pathServ[1]["text"]
            totalTime+=time
            
            try: 
                currentSeverity+= pathServ[0][c+round(totalTime)]
            except:
                currentSeverity+= pathServ[0][-1]

        bigListWeights.append(currentSeverity)
    return bigListWeights

