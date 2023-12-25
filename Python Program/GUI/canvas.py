from tkinter import*

root=Tk()
canvas=Canvas(root,width=400,height=300, bg="green")
canvas.pack()

line=canvas.create_line(0,0,200,200)
line2=canvas.create_line(200,100,0,200,fill="blue")
root.geometry("400x500+150+150")
root.mainloop()
