from tkinter import * 
from tkinter import messagebox 
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("ALERT","STOP! VIRUS FOUND")

    #adding button widget to window 
button= Button(root,text="scan for virus",command=msg)
button.place(x=40,y=80)
#entering main event loop
root.mainloop()