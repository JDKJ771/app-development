from tkinter import *
import pymysql as mdb
from tkinter import ttk

root = Tk()  
root.title("eCOMMAND")
root.minsize(800,500)
root.geometry("1200x800")


tree = ttk.Treeview(root)

# Database Call
dbi = mdb.connect("localhost",port=3306, user="user", passwd="*****", db="index_db" )
cursor = dbi.cursor()

tree["columns"] = ("one", "two", "three")
tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)


cursor.execute("""SELECT * FROM caution_elements""")
dbi.commit()

cpt = 0 
tree.insert('', 'end', values=(row[0], row[1], row[2]))
cpt += 1 # increment the ID
tree.pack()

photo = PhotoImage(file="test.png")
label = Label(root,image=photo)
label.pack()

root.mainloop() 
