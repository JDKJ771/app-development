import tkinter as tk
def hi():
    name=entry.get()
    print('hi', name)
root = tk.Tk()

textLabel = tk.Label(root, text = "hi put your name here: ")
textLabel.pack()
root.title("saying hi")
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root, text = 'done', command=hi)
button.pack()


root.mainloop()
