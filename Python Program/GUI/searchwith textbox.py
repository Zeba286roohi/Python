from tkinter import*
import wikipedia 
#to import wiki go to cmnd n type pip3 install wikipedia
def get_me():
    entry_value=entry.get()
    answer_value=wikipedia.summary(entry_value)
    answer.delete(1.0,END)
    answer.insert(INSERT,answer_value)
    
root=Tk()
topframe=Frame(root)
entry=Entry(topframe)
entry.pack()
button=Button(topframe,text="Search",command=get_me)
button.pack()



topframe.pack(side=TOP)
buttomframe=Frame(root)
scroll=Scrollbar(buttomframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(buttomframe,width=30,height=10,yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()

buttomframe.pack()
root.mainloop()
