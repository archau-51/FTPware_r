from tkinter import * 
from tkinter import messagebox
import sys
if sys.argv[1] == "0":
    root = Tk()
    root.geometry("300x200")
    w = Label(root, text =sys.argv[2], font = sys.argv[3], cnf = {"bg" : sys.argv[4], "fg" : sys.argv[5]})
    w.pack()
elif sys.argv[1] == "1":
    messagebox.showinfo(sys.argv[2], sys.argv[3])
  
root.mainloop()