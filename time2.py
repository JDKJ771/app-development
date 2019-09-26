#if reading this, start at the bottom and work to top.
#start
import tkinter as tk

root = tk.Tk()

def next():
    import mainapp

    #start def
def A9():
     textLabel = tk.Label(root, text = "what time does A3 start and end : ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'next', command=next)
    button.pack()

def A8():
    textLabel = tk.Label(root, text = "what time does A3 start and end : ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A8', command=A8)
    button.pack()

def A7():
    textLabel = tk.Label(root, text = "what time does A3 start and end : ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A8', command=A8)
    button.pack()

def A6():
    textLabel = tk.Label(root, text = "what time does A3 start and end: ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A7', command=A7)
    button.pack()
    
def A5():
   textLabel = tk.Label(root, text = "what time does A5 start and end: ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A6', command=A6)
    button.pack()

def A4():
    textLabel = tk.Label(root, text = "what time does A4 start and end : ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A5', command=A5)
    button.pack()

def A3():
    textLabel = tk.Label(root, text = "what time does A3 start and end : ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A4', command=A4)
    button.pack()
def A2():
    textLabel = tk.Label(root, text = "what time does A2 start and end: ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A3', command=A3)
    button.pack()
#end def 

button=tk.Button(root, text = 'A1')
button.pack()

textLabel = tk.Label(root, text = "what time does A1 start and end: ")
textLabel.pack()
root.title("Class sceadule")
entry=tk.Entry(root)
entry.pack()
entry=tk.Entry(root)
entry.pack()

button=tk.Button(root, text = 'A2', command=A2)
button.pack()
#end
root.mainloop()
