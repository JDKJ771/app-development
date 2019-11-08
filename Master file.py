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
    root.mainloop()
#end Def

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
     button=tk.Button(root, text = 'next', command=
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

A1 = entryA1.get

def the():
    textlable = tk.Lable(root,
    

#Main app

def mainapp():
    textLabel = tk.Label(root, text = "you are now all set up. use your phone as you would normaly would.") 
    textLabel = tk.Label(root, text = "we will alert you when you are all set up") 
    textLabel.pack()
    root.title("class sceaduler")
    button=tk.Button(root, text = 'see your classes!!!', command=the)
    button.pack()

    button=tk.Button(root, text = 'change your classes or add/subtract them', command=the)
    button.pack()

#time2

#end
root.mainloop()

