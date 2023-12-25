from tkinter import*
root=Tk()
def call_me(event):
    print("Im zeba")
button=Button(root,"click_me")
button.bind("<Button-1>",call_me)
button.pack()
root.mainloop()
