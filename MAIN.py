import latLongGrabber






if __name__=="__main__":
    StartLoc = input("Start Location: ")
    EndLoc = input("End Location: ")

    print(StartLoc)
    print(EndLoc)
    pointsOnPath = latLongGrabber.latLongGrabber((StartLoc,EndLoc))