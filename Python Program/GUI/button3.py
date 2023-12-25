from tkinter import*
root=Tk()
def right_click(event):
    print("Right click")
def left_click():
    print("Left click")
def middleClick(event):
    print("Middle click")
frame=Frame(root,width=300,height=300)
frame.bind("<Button-1>",left_click)
frame.bind("<Button-2>",right_click)
frame.bind("<Button-3>",middleClick)
frame.pack()
root.mainloop()
    
    
