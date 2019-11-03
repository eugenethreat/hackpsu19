

def weight(bigList,waitTime=3):

    bigListWeights = []

    for c in range(waitTime+1):
        totalTime = 0
        currentSeverity = 0

        for pathServ in bigList:

            time = pathServ[1]
            totalTime+=time

            try:
                currentSeverity+= pathServ[0][c+int(totalTime)]
            except:
                currentSeverity+= pathServ[0][-1]

        bigListWeights.append(currentSeverity)
    return bigListWeights
