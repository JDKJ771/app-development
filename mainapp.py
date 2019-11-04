import tkinter as tk

def the():
    import k

root = tk.Tk()

textLabel = tk.Label(root, text = "you are now all set up. use your phone as you would normaly would.") 
textLabel = tk.Label(root, text = "we will alert you when you are all set up") 
textLabel.pack()
root.title("class sceaduler")
button=tk.Button(root, text = 'see your classes!!!', command=the)
button.pack()

button=tk.Button(root, text = 'change your classes or add/subtract them', command=the)
button.pack()
the.print    
        
        
root.mainloop()
