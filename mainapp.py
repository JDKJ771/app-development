import tkinter as tk

root = tk.Tk()

textLabel = tk.Label(root, text = "you are now all set up. use your phone as you would normaly would.") 
textLabel = tk.Label(root, text = "we will alert you when you are all set up") 
textLabel.pack()
root.title("scheduler for classes")
entry=tk.Entry(root)
entry.pack()



root.mainloop()
