from tkinter import*
root =Tk()
frame=Frame(root)
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)
listbox=Listbox(frame,yscrollcommand=scroll.set)
for i in range (1,100):
    listbox.insert(END,"List"+ str(i))

    
listbox.pack(side=LEFT)
frame.pack()

scroll.config(command=listbox.yview)
root.geometry("400x400+120+120")
root.mainloop()
