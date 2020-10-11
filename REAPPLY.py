
from Tkinter import *
import sqlite3
from asn1crypto._ffi import null
from Finder.Type_Definitions import column
root = Tk()


def db_create():
    conn = sqlite3.connect('st.db')
    print("Opened successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS FINAL
    (NAME TEXT NOT NULL,
    POINTS INT,
    PASSWORD TEXT NOT NULL);''')
    print("Table has been created")


def choose(val):
    suin = Toplevel(root)
    print(val)
    d = val[0]
    e = val[1]
    f = val[2]
    def choiced():
    
        fies = Toplevel(root)
        searchSteps = open('Steps.txt').read().split('\n')
        dt = {}
        for gut in searchSteps :
            _gut = gut.split(" -+- ")
            _gut[1] = _gut[1].replace("&$&", "\n")
            dt[_gut[0]] = _gut[1]
        Label(fies, text = dt[d]).grid(rows = 1, column = 1)
        print dt[d]
        Button(fies, text = "Done").grid(row = 8, column = 8)
    def choicee():
    
        fies = Toplevel(root)
        searchSteps = open('Steps.txt').read().split('\n')
        dt = {}
        for gut in searchSteps :
            _gut = gut.split(" -+- ")
            _gut[1] = _gut[1].replace("&$&", "\n")
            dt[_gut[0]] = _gut[1]
        Label(fies, text = dt[e]).grid(rows = 1, column = 1)
        print dt[e]
        Button(fies, text = "Done").grid(row = 8, column = 8)
    def choicef():
    
        fies = Toplevel(root)
        searchSteps = open('Steps.txt').read().split('\n')
        dt = {}
        for gut in searchSteps :
            _gut = gut.split(" -+- ")
            _gut[1] = _gut[1].replace("&$&", "\n")
            dt[_gut[0]] = _gut[1]
        Label(fies, text = dt[f]).grid(rows = 1, column = 1)
        print dt[f]
        Button(fies, text = "Done").grid(row = 8, column = 8)
    Button(suin, text = d, command = choiced).grid(row = 2, column = 2)
    Button(suin, text = e, command = choicee).grid(row = 3, column = 2)
    Button(suin, text = f, command = choicef).grid(row = 4, column = 2)
def log_in():

    def checkdb(userInput):
        
        
        searchDatabase = open('DTABSE.txt').read().split('\n')
        diction = {}
        for content in searchDatabase:
            _content = content.split(" -+- ")
            diction[_content[0]] = _content[1]
        if userInput in diction.keys():
            val = diction[userInput].split(" =+= ")
            choose(val)

            
        else:
            print("Search results not found!")

            
    def search ():
        swin = Toplevel(root)
        conn = sqlite3.connect('st.db')
        print("Opened Successfully")
        a = e1.get()
        b = e2.get()
        rows = conn.execute("SELECT POINTS FROM FINAL WHERE NAME = '"+a+"' and PASSWORD = '"+b+"'")
        for col in rows:
            a = col[0]
        Label(swin, text = ("Current Points",a)).grid(row = 1, column = 5)
        sear = Entry(swin)
        sear.grid(row = 1, column = 1)
        def entryget ():
            print (sear.get())
            x = sear.get()
            checkdb(x)
        Label(swin, text = "").grid(row = 2, column = 1)
        Label(swin, text = "").grid(row = 3, column = 1)
        Label(swin, text = "").grid(row = 4, column = 1)
        Button(swin, text = "Search", command = entryget).grid(row = 8, column = 2)
        
    def check():
        conn = sqlite3.connect('st.db')
        print("Opened Successfully")
        sql = "SELECT NAME FROM FINAL WHERE NAME = '"+e1.get()+"' and PASSWORD = '"+e2.get()+"'"
        print(sql)
        c = conn.execute(sql)
        flag = 0
        for row in c:
            print ("Valid")
            flag = 1
            search()
        if flag ==0:
            print ("Invalid")
    swin = Toplevel(root)
    Label(swin, text = "Username").grid(row = 0)
    Label(swin, text = "Password").grid(row = 1)
    e1 = Entry(swin)
    e2 = Entry(swin, show ='*')
    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    Button(swin, text = 'Complete Log In', command = check).grid(row = 4, column = 0, pady = 4)
    
def sign_in():
    def insert():
        conn = sqlite3.connect('st.db')
        print("Opened Successfully")
        w = "0"
        sql = "INSERT INTO FINAL( NAME, PASSWORD, , POINTS) VALUES \
        ( '"+str(e1.get())+"', '"+str(e2.get())+"', '"+w+"')"
        print (sql)
        conn.execute(sql)
        conn.commit()
        print("Records have been created")

        conn.close()
    swin = Toplevel(root)
    photo = PhotoImage(file = "LOGO.gif")
    Label(root, image = photo).grid(row =1,column = 3)
    Label(swin, text = "Username").grid(row = 0)
    Label(swin, text = "Password").grid(row = 1)
    e1 = Entry(swin)
    e2 = Entry(swin, show ='*')

    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    Label(swin, text = "Age").grid(row = 2)
    Label(swin, text = "City").grid(row = 3)
    e3 = Entry(swin)
    e4 = Entry(swin)
    e3.grid(row = 2, column = 1)
    e4.grid(row = 3, column = 1)
    Button(swin, text = 'Complete Sign In', command = insert).grid(row = 4, column = 0, pady = 4)

photo = PhotoImage(file = "LOGO.gif")
Label(root, image = photo).grid(row =1,column = 3)
log = Button(root, text = "Log In", command = log_in).grid(row = 3, column = 3)
sig = Button(root, text = "Sign In", command = sign_in).grid(row = 4, column = 3)
db_create()
mainloop()