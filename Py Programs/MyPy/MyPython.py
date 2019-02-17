import tkinter 
from tkinter import *

class AlarmFrame(Frame):
    def repeater(self):                          
        self.bell()                              
        self.after(self.msecs, self.repeater)    
    def __init__(self, msecs=1000):              
        Frame.__init__(self)
        self.msecs = msecs
        self.pack()
        stopper = Button(self, text='Welcome to CSCI236!!!', command=self.quit, width=50,height=10)
        stopper.pack()
        stopper.config(bg='red', fg='white', bd=50) 
        self.stopper = stopper
        self.repeater()

class AlarmHide(AlarmFrame):      
    def repeater(self):      
        self.bell()          
        if self.shown:
            self.stopper.pack_forget()           
        else:                                    
            self.stopper.pack()
        self.shown = not self.shown              
        self.after(self.msecs, self.repeater)    
    def __init__(self, msecs=1000):              
        self.shown = 0
        AlarmFrame.__init__(self, msecs)
 
if __name__ == '__main__': 
     AlarmHide(msecs=500).mainloop()
