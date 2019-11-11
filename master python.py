#start
import tkinter as tk


root = tk.Tk()




#start def
def time2():
        #if reading this, start at the bottom and work to top.
    #start
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
    #this is the first
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
#end Def

    #C day
def cday():
    textLabel = tk.Label(root, text = "what are your C day classes: ")
    textLabel.pack()
    root.title("Class sceadule")

    entryC1=tk.Entry(root)
    entryC1.pack()

    entryC2=tk.Entry(root)
    entryC2.pack()

    entryC3=tk.Entry(root)
    entryC3.pack()

    button=tk.Button(root, text = 'skip', command=time2)
    button.pack()
    def c():
       
        Ce1 = entryC1.get()
        Ce2 = entryC2.get()
        Ce3 = entryC3.get()
            if Ce1 != (''):
                if Ce2 != (''):
                    if Ce3 != (''):
                            button=tk.Button(root, text = 'next', command=time2)
                            button.pack()

    button=tk.Button(root, text = 'check', command=c)
    





    
    #B day

def bday():
    textLabel = tk.Label(root, text = "what are your B day classes: ")
    textLabel.pack()
    root.title("Class sceadule")

    entryB1 = tk.Entry(root)
    entryB1.pack()

    entryB2 = tk.Entry(root)
    entryB2.pack()

    entryB3 = tk.Entry(root)
    entryB3.pack()

    entryB4 = tk.Entry(root)
    entryB4.pack()

    entryB5 = tk.Entry(root)
    entryB5.pack()

    entryB6 = tk.Entry(root)
    entryB6.pack()

    entryB7 = tk.Entry(root)
    entryB7.pack()

    entryB8 = tk.Entry(root)
    entryB8.pack()

    entryB9 = tk.Entry(root)
    entryB9.pack()

    def B():
        Be1 = entryB1.get()
        Be2 = entryB2.get()
        Be3 = entryB3.get()
        Be4 = entryB4.get()
        Be5 = entryB5.get()
        Be6 = entryB6.get()
        Be7 = entryB7.get()
        Be8 = entryB8.get()
        Be9 = entryB9.get()
        if Be1 != (''):
            if Be2 != (''):
                if Be3 != (''):
                    if Be4 != (''):
                        if Be5 != (''):
                            if Be6 != (''):
                                if Be7 != (''):
                                    if Be8 != (''):
                                        if Be9 != (''):
                                            button=tk.Button(root, text = 'next', command=cday)
                                            button.pack()
            
    

    button=tk.Button(root, text = 'check',command=B )
    button.pack()





      #A day  

def __init__(self):
    self.root = tk.Tk()
    self.label = tk.Label(text="")
    self.label.pack()
    self.update_clock()
    self.root.mainloop()

#end def


textLabel=tk.Label(root, text = "what are your A day classes: ")
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


def A():
    Ae1 = entryA1.get()
    Ae2 = entryA2.get()
    Ae3 = entryA3.get()
    Ae4 = entryA4.get()
    Ae5 = entryA5.get()
    Ae6 = entryA6.get()
    Ae7 = entryA7.get()
    Ae8 = entryA8.get()
    Ae9 = entryA9.get()
    if Ae1 != (''):
        if Ae2 != (''):
           if Ae3 != (''):
                if Ae4 != (''):
                      if Ae5 != (''):
                            if Ae6 != (''): 
                                    if Ae7 != (''):
                                            if Ae7 != (''):
                                                    if Ae8 != (''):
                                                            if Ae9 != (''):
                                                                    button=tk.Button(root, text = 'next', command=bday)
                                                                    button.pack()
button=tk.Button(root, text = 'check', command=A)
button.pack()
root.mainloop()
