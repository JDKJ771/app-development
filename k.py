#start
import tkinter as tk


root = tk.Tk()




#start def
def time2():
    import time2
    
#C day
def cday():
    textLabel = tk.Label(root, text = "what are your B day classes: ")
    textLabel.pack()
    root.title("Class sceadule")

    entryC1=tk.Entry(root)
    entryC1.pack()

    entryC2=tk.Entry(root)
    entryC2.pack()

    entryC3=tk.Entry(root)
    entryC3.pack()
    button=tk.Button(root, text = 'next', command=time2)
    button.pack()


#B day

def bday():
    textLabel = tk.Label(root, text = "what are your B day classes: ")
    textLabel.pack()
    root.title("Class sceadule")

    entryB1=tk.Entry(root)
    entryB1.pack()

    entryB2=tk.Entry(root)
    entryB2.pack()

    entryB3=tk.Entry(root)
    entryB3.pack()

    entryB4=tk.Entry(root)
    entryB4.pack()

    entryB5=tk.Entry(root)
    entryB5.pack()
    
    entryB6=tk.Entry(root)
    entryB6.pack()

    entryB7=tk.Entry(root)
    entryB7.pack()

    entryB8=tk.Entry(root)
    entryB8.pack()

    entryB9=tk.Entry(root)
    entryB9.pack()
    button=tk.Button(root, text = 'next', command=cday)
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
#end def
textLabel = tk.Label(root, text = "What are your A day classes: ")
textLabel.pack()
root.title("Class sceadule")

entryA1=tk.Entry(root)
entryA1.pack()
   
entryA2=tk.Entry(root)
entryA2.pack()

entryA3=tk.Entry(root)
entryA3.pack()

entryA4=tk.Entry(root)
entryA4.pack()

entryA5=tk.Entry(root)
entryA5.pack()
    
entryA6=tk.Entry(root)
entryA6.pack()

entryA7=tk.Entry(root)
entryA7.pack()

entryA8=tk.Entry(root)
entryA8.pack()

entryA9=tk.Entry(root)
entryA9.pack()
button=tk.Button(root, text = 'next', command=bday)
button.pack()



#Main app

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

#time2

#end
root.mainloop()

