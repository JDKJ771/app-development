from tkinter import * 

def show():
    p = password.get() #get password from entry
    print(p)


app = Tk()   
password = StringVar() #Password variable
passEntry = Entry(app, textvariable=password, show='*').pack() 
submit = Button(app, text='Show Console',command=show).pack()      
app.mainloop() 
