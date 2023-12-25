from tkinter import*

def click_me():
    print(spin1.get())
root=Tk()

spin1=Spinbox(root,from_=1, to=5)
spin1.pack()
button=Button(root,text="print", command=click_me).pack()
root.geometry("300x300")
root.mainloop()
