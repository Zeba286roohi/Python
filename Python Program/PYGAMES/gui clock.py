from tkinter import*
import time
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
#app_window.resizable(1,1)

text_font= ("Airel", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")#The strftime() method returns a string representing date and time using date, time or datetime
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
