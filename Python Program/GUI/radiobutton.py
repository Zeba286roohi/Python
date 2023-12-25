#RADIO BUTTONS
from tkinter import*
def click_me():
    if(i.get()==1):
        print("You are male")
    else:
         print("You are female")
root=Tk()
i=IntVar()
r1=Radiobutton(root,text="male",value=1,variable=i)
r2=Radiobutton(root,text="female",value=2,variable=i)
r1.pack()
r2.pack()


button=Button(root,text="Clickhere",command=click_me)
button.pack()
root.geometry("300x300+120+120")
root.mainloop()
