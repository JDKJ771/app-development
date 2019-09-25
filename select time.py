import tkinter as tk

root = tk.Tk()

def A3():
    textLabel = tk.Label(root, text = "what time do these classes start and end: ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A4', command=A2)
    button.pack()
def A2():
    textLabel = tk.Label(root, text = "what time do these classes start and end: ")
    textLabel.pack()
    root.title("Class sceadule")
    entry=tk.Entry(root)
    entry.pack()
    entry=tk.Entry(root)
    entry.pack()
    button=tk.Button(root, text = 'A3', command=A3)
    button.pack()

    

textLabel = tk.Label(root, text = "what time do these classes start and end: ")
textLabel.pack()
root.title("Class sceadule")
entry=tk.Entry(root)
entry.pack()
entry=tk.Entry(root)
entry.pack()

button=tk.Button(root, text = 'A2', command=A2)
button.pack()
