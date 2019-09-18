import tkinter as tk
import datetime

today = datetime.datetime.now()


root = tk.Tk()
#B day
def bday():
    textLabel = tk.Label(root, text = "what are your B day classes: ")
    textLabel.pack()
    root.title("Class sceadule")

    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()
    
    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()

    entry=tk.Entry(root)
    entry.pack()
  #A day  
textLabel = tk.Label(root, text = "What are your A day classes: ")
textLabel.pack()
root.title("Class sceadule")
entry=tk.Entry(root)
entry.pack()
entry=tk.Entry(root)
entry.pack()

entry=tk.Entry(root)
entry.pack()

entry=tk.Entry(root)
entry.pack()

entry=tk.Entry(root)
entry.pack()
    
entry=tk.Entry(root)
entry.pack()

entry=tk.Entry(root)
entry.pack()

entry=tk.Entry(root)
entry.pack()

entry=tk.Entry(root)
entry.pack()
button=tk.Button(root, text = 'done', command=bday)
button.pack()




root.mainloop()
