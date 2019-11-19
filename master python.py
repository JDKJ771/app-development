#start
import tkinter as tk
root = tk.Tk()
#start def
def time2():
        #if reading this, start at the bottom and work to top.
    #start
        #start def
 def BTime():
    #BDAY!!!!!!!!
        def B9():
            textLabel = tk.Label(root, text = "what time does B9 start and end : ")
            textLabel.pack()
            root.title("Class sceadule")
            entry=tk.Entry(root)
            entry.pack()
            entry=tk.Entry(root)
            entry.pack()
            button1=tk.Button(root, text = 'next', command=next)
            button1.pack()
        def B8():
            textLabel = tk.Label(root, text = "what time does B8 start and end : ")
            textLabel.pack()
            root.title("Class sceadule")
            entry=tk.Entry(root)
            entry.pack()
            entry=tk.Entry(root)
            entry.pack()
            button2=tk.Button(root, text = 'B9', command=B9)
            button2.pack()
        def B7():
            textLabel = tk.Label(root, text = "what time does B7 start and end : ")
            textLabel.pack()
            root.title("Class sceadule")
            entry=tk.Entry(root)
            entry.pack()
            entry=tk.Entry(root)
            entry.pack()
            button3=tk.Button(root, text = 'B8', command=B8)
            button3.pack()
        def B6():
            textLabel = tk.Label(root, text = "what time does B6 start and end: ")
            textLabel.pack()
            root.title("Class sceadule")
            entry=tk.Entry(root)
            entry.pack()
            entry=tk.Entry(root)
            entry.pack()
            button4=tk.Button(root, text = 'B7', command=B7)
            button4.pack()
        def B5():
            textLabel = tk.Label(root, text = "what time does B5 start and end: ")
            textLabel.pack()
            root.title("Class sceadule")
            entry=tk.Entry(root)
            entry.pack()
            entry=tk.Entry(root)
            entry.pack()
            button5=tk.Button(root, text = 'B6', command=B6)
            button5.pack()
        def B4():
            textLabel = tk.Label(root, text = "what time does B4 start and end : ")
            textLabel.pack()
            root.title("Class sceadule")
            entryA4time1=tk.Entry(root)
            entryA4time1.pack()
            entryA4time2=tk.Entry(root)
            entryA4time2.pack()
            button6=tk.Button(root, text = 'B5', command=B5)
            button6.pack()
        def B3():
            textLabel = tk.Label(root, text = "what time does B3 start and end : ")
            textLabel.pack()
            root.title("Class sceadule")
            entryA3time1=tk.Entry(root)
            entryA3time1.pack()
            entryA3time2=tk.Entry(root)
            entryA3time2.pack()
            button7=tk.Button(root, text = 'B4', command=B4)
            button7.pack()
        def B2():
            textLabel = tk.Label(root, text = "what time does B2 start and end: ")
            textLabel.pack()
            root.title("Class sceadule")
            entryA2time1=tk.Entry(root)
            entryA2time1.pack()
            entryA2time2=tk.Entry(root)
            entryA2time2.pack()
            button8=tk.Button(root, text = 'B3', command=B3)
            button8.pack()
            #end def 
            #this is the first
            button9=tk.Button(root, text = 'B1')
            button9.pack()
            textLabel = tk.Label(root, text = "what time does B1 start and end: ")
            textLabel.pack()
            root.title("Class sceadule")
            entryA1time1=tk.Entry(root)
            entryA1time1.pack()
            entryA1time2=tk.Entry(root)
            entryA1time2.pack()
            button10=tk.Button(root, text = 'B2', command=B2)
            button10.pack()
    #ADAY
 def ATime():
            def A9():
                textLabel = tk.Label(root, text = "what time does A9 start and end : ")
                textLabel.pack()
                root.title("Class sceadule")
                entry=tk.Entry(root)
                entry.pack()
                entry=tk.Entry(root)
                entry.pack()
                button11=tk.Button(root, text = 'B days', command=Btime)
                button11.pack()
            def A8():
                textLabel = tk.Label(root, text = "what time does A8 start and end : ")
                textLabel.pack()
                root.title("Class sceadule")
                entry=tk.Entry(root)
                entry.pack()
                entry=tk.Entry(root)
                entry.pack()
                button12=tk.Button(root, text = 'A9', command=A9)
                button12.pack()
            def A7():
                textLabel = tk.Label(root, text = "what time does A7 start and end : ")
                textLabel.pack()
                root.title("Class sceadule")
                entry=tk.Entry(root)
                entry.pack()
                entry=tk.Entry(root)
                entry.pack()
                button13=tk.Button(root, text = 'A8', command=A8)
                button13.pack()
            def A6():
                textLabel = tk.Label(root, text = "what time does A6 start and end: ")
                textLabel.pack()
                root.title("Class sceadule")
                entry=tk.Entry(root)
                entry.pack()
                entry=tk.Entry(root)
                entry.pack()
                button14=tk.Button(root, text = 'A7', command=A7)
                button14.pack()
            def A5():
                textLabel = tk.Label(root, text = "what time does A5 start and end: ")
                textLabel.pack()
                root.title("Class sceadule")
                entry=tk.Entry(root)
                entry.pack()
                entry=tk.Entry(root)
                entry.pack()
                button15=tk.Button(root, text = 'A6', command=A6)
                button15.pack()
            def A4():
                textLabel = tk.Label(root, text = "what time does A4 start and end : ")
                textLabel.pack()
                root.title("Class sceadule")
                entryA4time1=tk.Entry(root)
                entryA4time1.pack()
                entryA4time2=tk.Entry(root)
                entryA4time2.pack()
                button16=tk.Button(root, text = 'A5', command=A5)
                button16.pack()
            def A3():
                textLabel = tk.Label(root, text = "what time does A3 start and end : ")
                textLabel.pack()
                root.title("Class sceadule")
                entryA3time1=tk.Entry(root)
                entryA3time1.pack()
                entryA3time2=tk.Entry(root)
                entryA3time2.pack()
                button17=tk.Button(root, text = 'A4', command=A4)
                button17.pack()
            def A2():
                textLabel = tk.Label(root, text = "what time does A2 start and end: ")
                textLabel.pack()
                root.title("Class sceadule")
                entryA2time1=tk.Entry(root)
                entryA2time1.pack()
                entryA2time2=tk.Entry(root)
                entryA2time2.pack()
                button18=tk.Button(root, text = 'A3', command=A3)
                button18.pack()
            #end def 
            #this is the first
            button19=tk.Button(root, text = 'A1')
            button19.pack()
            textLabel = tk.Label(root, text = "what time does A1 start and end: ")
            textLabel.pack()
            root.title("Class sceadule")
            entryA1time1=tk.Entry(root)
            entryA1time1.pack()
            entryA1time2=tk.Entry(root)
            entryA1time2.pack()
            button20=tk.Button(root, text = 'A2', command=A2)
            button20.pack()
    #end
#end Def
def hi():
        window = tk.Toplevel(root)
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
            button21=tk.Button(root, text = 'skip', command=time2)
            button21.pack()
            def c():
                Ce1 = entryC1.get()
                Ce2 = entryC2.get()
                Ce3 = entryC3.get()
                if Ce1 != (''):
                        if Ce2 != (''):
                            if Ce3 != (''):
                                    button22=tk.Button(root, text = 'next', command=time2)
                                    button22.pack()
            button23=tk.Button(root, text = 'check', command=c)
            button23.pack()
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
                                                    button24=tk.Button(root, text = 'next', command=cday)
                                                    button24.pack()
            button25=tk.Button(root, text = 'check',command=B )
            button25.pack()
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
                                                                            button26=tk.Button(root, text = 'next', command=bday)
                                                                            button26.pack()
        button27=tk.Button(root, text = 'check', command=A)
        button27.pack()
textLabel=tk.Label(root, text = "choose one ")
textLabel.pack()
root.title("Class sceadule")
button=tk.Button(root,text = 'mix of both', command=hi)
button=tk.Button(root, text = 'middle school', command=hi)
button.pack()
button=tk.Button(root, text = 'high school', command=hi)
button.pack()
root.mainloop()
