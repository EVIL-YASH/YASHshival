# Widget --> Button,Canvas,CheckButton,Entry,Frame,Label,Listbox,Menu,MenuButton
#            Message,RaidioButton,Scale,ScrollBar,Text,TopLevel,LabelFrame,MessageBox


# Geometry Managers : --> pack() , grid() ,place()


#place()
import tkinter as tk

win=tk.Tk()
win.title("JAI HIND")
win.geometry("1920x1200")

# add frame1
frame1=tk.Frame(master=win,width=50,height=110,bg="orange")
frame1.pack(fill=tk.X) # fill=tk.X,tk.Y,tk.BOTH

# add frame2
frame2=tk.Frame(master=win,width=10000,height=100,bg="green")
frame2.pack(side=tk.BOTTOM)


# add frame3
frame3=tk.Frame(master=win,width=50,height=50,bg="navy blue")
frame3.pack(expand=True)



win.mainloop()