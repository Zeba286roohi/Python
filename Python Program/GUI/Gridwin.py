from tkinter import*
root=Tk()

title=Label(root,text="Enter your Info:").grid()
firstlabel=Label(root,text="First Name:",width=20,bg="aqua").grid(row=1,column=0)
firstNameEntry=Entry(root).grid(row=0,column=1)


lastlabel=Label(root,text="Last Name:",bg="green").grid(row=2,column=0)
lasttNameEntry=Entry(root).grid(row=1,column=1)


emaillabel=Label(root,text="Email:",bg="yellow").grid(row=3,column=0)
emailtNameEntry=Entry(root).grid(row=3,column=1)

button=Button(root,text="Submit").grid(row=4,column=2)


root.mainloop()