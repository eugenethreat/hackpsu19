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
def forget(event):
    event.widget.pack_forget()
def clicked():
    #res = "Welcome to " + txt.get()

    startLoc = start.get()
    endLoc = end.get()
    
    if(startLoc!="" and endLoc !=""):
        startLoc.rstrip()
        startLoc.lstrip()
        endLoc.rstrip()
        endLoc.lstrip()

        lbl = Label(window, text="Finding safest time to depart...")
        lbl.grid(column=1, row=2)
        waitTime = LTAT.main(startLoc,endLoc)
        
        if(waitTime==0):
            pText = ("The best time for you to leave for " +str(endLoc)+" would be now.")
        else:
            pText = "The best time for you to leave for " +str(endLoc)+" would be in "+str(waitTime)+" hour"+ ("s"if waitTine>1 else "")

        lbl = Label(window, text=pText)
        lbl.grid(column=1, row=4)


btn = Button(window, text="Search", command=clicked)
btn.grid(column=2, row=1)



window.mainloop()