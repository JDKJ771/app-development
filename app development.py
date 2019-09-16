import tkinter as tk
def hi():
    name=entry.get()
    print('hi', name)
root = tk.Tk()

textLabel = tk.Label(root, text = "put your A day classes here: ")
textLabel.pack()
root.title("scheduler for classes")
entry=tk.Entry(root)
entry.pack()



root.mainloop()
