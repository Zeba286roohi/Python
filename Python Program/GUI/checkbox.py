from tkinter import*

def click_here():
    print(i.get())
    
root=Tk()

i=IntVar()
c=Checkbutton(root,text="item",variable=i,offvalue="unchecked",onvalue="checked")
c.pack()


button=Button(root,text="click me",command=click_here)
button.pack()
root.geometry("300x300+120+120")
root.mainloop()
