from tkinter import*

class myButtons:
    def __init__(self, master): 
        self.printButton=Button(master, text="print", command=self.printMessage)
        self.printButton.pack()
        
        self.quitButton=Button(master,text="quit",command=master.quit)
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
            print("print message")
                            
root=Tk()
b=myButtons(root)
root.mainloop()
