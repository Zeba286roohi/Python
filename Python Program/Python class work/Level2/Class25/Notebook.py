from tkinter import * 
from tkinter import messagebox 
from PIL import ImageTk ,Image
# Part 1 creating all type of message boxes
"""root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='CodeVidhya', font = "50")  
w.pack() 

messagebox.showinfo("showinfo", "Information") 
  
messagebox.showwarning("showwarning", "Warning") 
  
messagebox.showerror("showerror", "Error") 
  
messagebox.askquestion("askquestion", "Are you sure?") 
  
messagebox.askokcancel("askokcancel", "Want to continue?") 
  
messagebox.askyesno("askyesno", "Find the value?") 
  
messagebox.askretrycancel("askretrycancel", "Try again?")   
root.mainloop()

# Part 2 taking response from each box.
root = Tk() 
root.geometry("300x200") 
  
def func(boxtype ,response):
    Label(root, text =boxtype+ " gives the message " + str(response) ).pack()
response = messagebox.showinfo("showinfo", "Information") 
func("showinfo" ,response )
response = messagebox.showwarning("showwarning", "Warning") 
func("showwarning" ,response )
response = messagebox.showerror("showerror", "Error") 
func("showerror" ,response )  
response = messagebox.askquestion("askquestion", "Are you sure?") 
func("askquestion" ,response )
response = messagebox.askokcancel("askokcancel", "Want to continue?") 
response = func("askokcancel" ,response ) 
messagebox.askyesno("askyesno", "Find the value?") 
func("askyesno" ,response )  
response = messagebox.askretrycancel("askretrycancel", "Try again?")  
func("askretrycancel" ,response )  
root.mainloop()
"""
#Part 3 Adding new window ==========================================
root = Tk()

def open():
    global myimage
    myimage = ImageTk.PhotoImage(Image.open("C:/Users/arpit/Dropbox/Codevidhya/Lecture 26/paul.png"))
    top = Toplevel()
    top.geometry("300x400")
    Button(top , text = "Close Window" , command = top.destroy).pack()
    Label(top, image = myimage).pack()
root.geometry("300x400")
Button(root, text ="Open second Window" , command = open).pack()
mainloop()