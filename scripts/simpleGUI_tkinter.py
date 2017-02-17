#!/usr/bin/python
#This is using Tkinter

import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0, row=0, stick='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        
        button = Tkinter.Button(self,text=u"Click me !", command=self.OnButtonClick)
        button.grid(column=1, row=0)
        
        label = Tkinter.Label(self,
                              anchor="w",
                              fg="white",
                              bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
    
    def OnButtonClick(self):
        print "You Clicked the Button"
    
    def OnPressEnter(self, event):
        print "You Pressed Enter"
        

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Simple GUI')
    app.mainloop()