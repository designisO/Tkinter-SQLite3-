from tkinter import *
import sqlite3

# connecting to db
connection = sqlite3.connect("details.db")
cursor = connection.cursor()

# creating a table called users
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, firstname text NOT NULL, email text NOT NULL); """)

# function of the "add" button
def add_new_user():
    newfirstname = firstname.get()
    newemail = email.get()
    
    # selecting users in the db added.
    cursor.execute("SELECT COUNT(*) from users WHERE firstname = '" + newfirstname + "' ")
    result = cursor.fetchone()
    
    # created the email error if duplicates occur.
    if int(result[0]) > 0:
        error["text"] = "ERROR: Email already exist."
    else:
        error["text"] = "Added New Member"
        cursor.execute("INSERT INTO users(firstname, email) VALUES(?,?)",(newfirstname, newemail))
        connection.commit()
        
        # clear the fields once the users are added.
        firstname.delete(0, END)
        email.delete(0, END)

gui = Tk()
gui.title("Signup Now")
gui.geometry("450x180")

error = Message(text="", width=160)
error.place(x = 30, y = 10)
error.config(padx=0)


label1 = Label(text = "Enter Name: ")
label1.place(x = 30, y = 40)
label1.config(bg='lightblue', padx=0)

firstname = Entry(text = "")
firstname.place(x=150, y=40, width=200, height=25)

label1 = Label(text = "Enter Email Address: ")
label1.place(x = 30, y = 80)
label1.config(bg='lightblue', padx=0)

email = Entry(text = "")
email.place(x=150, y=80, width=200, height=25)

button = Button(text = "Add", command = add_new_user)
button.place(x=150, y=120, width=75, height=35)



gui.mainloop()
