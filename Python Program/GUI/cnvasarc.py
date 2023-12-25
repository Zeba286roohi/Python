from tkinter import*

root=Tk()
canvas=Canvas(root,width=400,height=400, bg="green")
canvas.pack()

canvas.create_arc(100,100,200,200,extent=270)

root.mainloop()
