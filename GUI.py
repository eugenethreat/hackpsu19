from tkinter import *

import LTAT


window = Tk()
window.title("Lets Take A Trip")
window.geometry('350x300')

lbl = Label(window, text="Starting Location")
lbl.grid(column=0, row=0)
start = Entry(window,width=30)
start.grid(column=1, row=0)
lbl = Label(window, text="Ending Location")
lbl.grid(column=0, row=1)
end = Entry(window,width=30)
end.grid(column=1, row=1)


img = PhotoImage(file = r"accuweather.png") 
img = img.subsample(10, 10) 
label = Label(image=img)
label.place(x=40, y=100, relwidth=1, relheight=1)



def clicked():


    startLoc = start.get()
    endLoc = end.get()
    lbl = Label(window, text="\n\n")
    lbl.grid(column=1, row=3)
    lblP = Label(window, text="      When should you leave?       \n                                 ")
    lblP.grid(column=1, row=4)

    if(startLoc!="" and endLoc !=""):
        startLoc.rstrip()
        startLoc.lstrip()
        endLoc.rstrip()
        endLoc.lstrip()

        lbl = Label(window, text="Finding safest time to depart...")
        lbl.grid(column=1, row=2)
        window.update()

        waitTime = LTAT.main(startLoc,endLoc)
        
        if(waitTime==0):
            pText = ("The best time for you to leave for\n " +str(endLoc)+" would be NOW.")
        else:
            pText = "The best time for you to leave for\n " +str(endLoc)+" would be in "+str(waitTime)+" HOUR"+ ("S"if waitTine>1 else "")

        
        lblP.configure(text = pText)


btn = Button(window, text="Search", command=clicked)
btn.grid(column=2, row=1)



window.mainloop()