from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
"""
#Part 1 opening files =================================================
root = Tk()

# Create open dialog box function
def open_image():
	#Open File Dialog Box
	root.filename = filedialog.askopenfilename(initialdir='C:/Users/arpit\Dropbox\Codevidhya\Lecture 27', title="Open An Image File", filetypes=( ("PNG File", "*.png"), ("All Files", "*.*") ))
	#my_label = Label(root, text=root.filename).pack(pady=10)
	global my_img
	# Open image and place on screen
	my_img = ImageTk.PhotoImage(Image.open(root.filename))
	img_label = Label(root, image=my_img)
	img_label.pack(pady=10)

my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)
root.mainloop()
"""
# Part 2 asksaveasfile() ==============================================
# importing all files  from tkinter 
from tkinter import * 
from tkinter import ttk 
  
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 
  
root = Tk() 
root.geometry('200x150') 
  
# function to call when user press 
# the save button, a filedialog will 
# open and ask to save file 
def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 
  
btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
btn.pack(side = TOP, pady = 20) 
  
mainloop() 
# Part 3 horizontal silder
"""
root = Tk()   
root.geometry("400x300")  
v1 = DoubleVar() 
  
def show1():        
    sel = "Horizontal Scale Value = " + str(v1.get()) 
    l1.config(text = sel, font =("Courier", 14))   
  
s1 = Scale( root, variable = v1,from_ = 1, to = 100,orient=HORIZONTAL)   
l3 = Label(root, text = "Horizontal Scaler") 
b1 = Button(root, text ="Display Horizontal",  
            command = show1,  
            bg = "yellow")   
  
l1 = Label(root) 
s1.pack(anchor = CENTER)  
l3.pack() 
b1.pack(anchor = CENTER) 
l1.pack()  
  
root.mainloop() 
"""