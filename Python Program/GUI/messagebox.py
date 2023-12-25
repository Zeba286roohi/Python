from tkinter import*
from tkinter import messagebox

def callme():
    messagebox.showinfo("Success","installation error")
    answer=messagebox.askyesnocancel("Exit","Do you want to exit")
    print(answer)
    if answer=='True':
        root.quit()
    
root=Tk()
b=Button(root,text="message",command=callme)
b.pack()
root.geometry("400x400+120+120")
root.mainloop()
