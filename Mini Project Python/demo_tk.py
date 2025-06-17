import tkinter as tk
from tkinter import ttk

def value():
    print(entry.get())


window=tk.Tk() #! root
window.title('Tic Tac Toc')
# window.geometry('300x300')

entry=ttk.Entry(master=window)
entry.pack() #! enter user input

button=ttk.Button(master=window, text="submit",command=value)
button.pack() #! simple button

window.mainloop()
