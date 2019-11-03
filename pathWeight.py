
bigList = [[[1,2,3,1],0],[[1,2,3,1],1],[[1,2,3,1],1]]

#waitTime = 3


def weight(bigList,waitTime=3):

    bigListWeights = []
    MAXTIME = len(bigList[0][0])

    for c in range(waitTime+1):
        totalTime = 0
        currentSeverity = 0

        for pathServ in bigList:
            time= pathServ[1]
            totalTime+=time
            #if(totalTime>MAXTIME):
                #totalTime = MAXTIME
            try:
                currentSeverity+= pathServ[0][c+int(totalTime)]
            except:
                currentSeverity+= pathServ[0][-1]
        bigListWeights.append(currentSeverity)
    return bigListWeights
