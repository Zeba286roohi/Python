from tkinter import*

root=Tk()
canvas=Canvas(root,width=400,height=400, bg="green")
canvas.pack()
canvas.create_rectangle(100,100,250,200,fill="red",outline="yellow")

root.mainloop()
