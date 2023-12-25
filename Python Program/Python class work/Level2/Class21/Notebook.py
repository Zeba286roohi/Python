from tkinter import *
#from tkinter.ttk import * 
#===================================================
# Part 1
"""
root = Tk()
def myclick():
    myLabel = Label(root, text = "You Clicked")
    myLabel.pack()
button = Button(root , text = "Click Me!",padx = 50 , pady = 20 ,command = myclick)
button.pack()
root.mainloop()

#======================================================
# Part 2
root = Tk() 
root.geometry('100x100') 
# This will create style object 
style = Style() 
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'), 
                foreground = 'red') 
# Style will be reflected only on  
# this button because we are providing 
# style only on this Button. 
''' Button 1'''
btn1 = Button(root, text = 'Quit !',  
                style = 'W.TButton', 
             command = root.destroy) 
btn1.grid(row = 0, column = 3, padx = 100) 
''' Button 2'''
btn2 = Button(root, text = 'Click me !', command = None) 
btn2.grid(row = 1, column = 3, pady = 10, padx = 100) 
root.mainloop()
#========================================================
# Part 3
root = Tk()
button = Button(root , text = "Click Me!" ,activebackground ="Blue", activeforeground = "Green",fg = "red" , bg ="black")
button.pack()
root.mainloop()
"""
#=======================================================
# Part 4 Creating Entry Widget
root = Tk()
e = Entry(root ,width = 50)
e.pack()
def myclick():
    myLabel = Label(root, text = "Hi!" + e.get())
    myLabel.pack()
button = Button(root , text = "Enter you name",padx = 50 , pady = 20 ,command = myclick)
button.pack()
root.mainloop()