from Tkinter import *
from simplex import  Simplex
from textOperator import Operator

vertices = []

def decision_mode():
    if e2.get()=='':
        create_simple_structure()
        return
    else:
        create_complete_structure()

def create_complete_structure():
    operator=Operator()
    for i in range(int(e1.get())):
        objGraph = Simplex(str(i + 1))
        vertices.append(objGraph)
    operator.create_complete_connection(e2.get(), vertices)
    operator.show_structures(vertices)
    return

def create_simple_structure():
    operator=Operator()
    for i in range(int(e1.get())):
        objGraph = Simplex(str(i + 1))
        vertices.append(objGraph)
    operator.create_simple_connection(e3.get(), vertices)
    operator.show_structures(vertices)
    return

def delVertices():
    operator=Operator()
    if(len(e4.get()) > 2):
        operator.delete_connection(e4.get(), vertices)
        operator.show_structures(vertices)
    return




master = Tk()
master.title = "master"
Label(master, text="enter number of vertices").grid(row=0)
Label(master, text="enter complete connection without "+"'.'").grid(row=1)
Label(master, text="enter connection with "+"'.'").grid(row=2)
Label(master, text="enter connection for delete with "+"'.'").grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=4, column=1)

Button(master, text='Quit', command=master.quit).grid(row=9, column=0)
Button(master, text='Create', command=decision_mode).grid(row=9, column=1)
Button(master, text='Delete', command=delVertices).grid(row=10, column=1)

master.wm_title("Simplex Tree")
mainloop()