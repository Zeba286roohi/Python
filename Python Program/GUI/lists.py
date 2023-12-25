from tkinter import*
def click_me():
    click_items=l.curselection()
    print(click_items)
    for item in click_items:
        print(l.get(item))
def delete_me():
    click_items=l.curselection()
    print(click_items)
    for item in click_items:
        print(l.delete(item))
        
              
root=Tk()
l=Listbox(root,width=30,height=15,selectmode=MULTIPLE)#typeof selectmode: single,multiple,extended
l.insert(1,"C++")
l.insert(2,"C")
l.insert(3,"Python")
l.insert(4,"Java")
l.insert(5,"C#")
l.pack()
button=Button(root,text="click",command=click_me)
button.pack()
button1=Button(root,text="delete",command=delete_me)
button1.pack()

root.geometry("400x400+120+120")
root.mainloop()
              
