# Geometry Managers : -->  grid() 

import tkinter as tk

win=tk.Tk()
win.title("Mandir Wahi Banega")
win.geometry("1180x720")
for i in range(11):
    for j in range(12):
        frame=tk.Frame(master=win,relief=tk.RAISED,borderwidth=4)
        frame.grid(row=i,column=j,padx=10,pady=10)
        label=tk.Label(master=frame,text=f"JAI SHRI {i} \n RAM {j}")
        label.pack()
win.mainloop()