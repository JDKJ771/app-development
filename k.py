import tkinter as tk


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
    button=tk.Button(root, text = 'next', command=time2)
    button.pack()


  #A day  

def __init__(self):
    self.root = tk.Tk()
    self.label = tk.Label(text="")
    self.label.pack()
    self.update_clock()
    self.root.mainloop()

def update_clock(self):
    now = time.strftime("%H:%M:%S")
    self.label.configure(text=now)
    self.root.after(1000, self.update_clock)

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
button=tk.Button(root, text = 'next', command=bday)
button.pack()



def time2():
    import time2

root.mainloop()

