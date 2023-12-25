from tkinter import*
from tkinter.font import Font
root=Tk()
my_font=Font(size=16,family="Times New Roman",weight="bold",slant="italic",underline=1)
label=Label(root,text="CodeVidhya",font=my_font).pack()

root.geometry("400x400+120+120")
root.mainloop()
              
