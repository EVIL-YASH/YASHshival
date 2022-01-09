from tkinter import *
from tkinter import ttk   # it is a theam for our application
from tkinter import font
import time # after importing we can use time
import datetime

def quit(*args):
    root.destroy()

def clock_time():
    
    time=datetime.datetime.now() # show date or time
    time = (time.strftime("Date :  %d -%m -%y \n Time  : %H:%M:%S")) # We want hour minutes seconds
    txt.set(time) # Display time
    root.after(1000,clock_time)
root=Tk() # this is theam for gui
 #root.attributes("-fullscreen",False)
root.configure(background="black")
root.bind("x",quit)
root.geometry("1000x300")
root.after(1000,clock_time)
root.title("Digital clock")


ft=font.Font(family="Arial", size=100,slant="italic")
txt=StringVar() # hold string Value
ft1=font.Font(family="Arial", size=50,slant="italic")
Label(root,text="Made by \n SHUBHAM NAGAWADE",background="yellow",font=ft1).pack()
lbl=ttk.Label(root,textvariable=txt,font=ft,foreground="red",background="white")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
