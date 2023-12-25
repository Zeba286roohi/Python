from tkinter import*
import sqlite3
connection=sqlite3.connect("details.db")
crsr=connection.cursor()


'''sql_command="""CREATE TABLE users(
id INTEGER PRIMARY KEY,
username VARCHAR(20),
password VARCHAR(20));"""
crsr.execute(sql_command)'''


def add_new_user():
    newUsername=username.get()
    newPassword=password.get()
    crsr.execute("select *from users where username='"+newUsername+"'")
    result=crsr.fetchone()
    if int(result[0])>0:
        error["text"]="Error:Username akready exists"
    else:
        error["text"]="Added New User"
        crsr.execute("INSERT INTO users(username,password)VALUES(?,?)",(newUsername,newPassword))
        connection.commit()
        username.delete(0,END)
        password.delete(0,END)
        
root=Tk()
root.geometry("450x180")
error=Message(text="",width=160)
error.place(x=30,y=10)
error.config(padx=0)

l1=Label(text="Ente Username:")
l1.place(x=30,y=40)
l1.config(bg='lightgreen',padx=0)
username=Entry(text="")
username.place(x=150,y=40,width=200,height=25)

l2=Label(text="Ente Password:")
l2.place(x=30,y=80)
l2.config(bg='lightgreen',padx=0)
password=Entry(text="")
password.place(x=150,y=80,width=200,height=25)
button=Button(text="Add",command=add_new_user)
button.place(x=150,y=120,width=75,height=35)


















root.mainloop()
