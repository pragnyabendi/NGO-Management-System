from tkinter import *
import tkinter.messagebox as msg

def login(frame):
    
    frame.grid_forget()
    frame.grid(row=3, column=1, columnspan=4)
    
    Label(frame, text="Admin ID: ", bg='#ceb180').grid(row=1, column=1)
    Label(frame, text="Password: ", bg='#ceb180').grid(row=2, column=1)

    global id, password
    
    id = Entry(frame)
    id.grid(row=1, column=2)

    password = Entry(frame, show="*")
    password.grid(row=2, column=2)
    
    next_button = Button(frame, text="Log in", command=admin_login)
    next_button.grid(row=4, column=4)

def admin_login():
    if(len(id.get())==0 or len(password.get())==0):
        return msg.showerror('NMS says', "Invalid Input!")
    
    id.delete(0, END)
    password.delete(0, END)

    admin_page = Tk()
    admin_page.configure(bg='#ceb180')

    Button(admin_page, text="Logout", command=admin_page.destroy).grid(row=1, column=4)
    Label(admin_page, text=" ", padx=30, bg='#ceb180').grid(row=2, column=1)
    Label(admin_page, text=" ", padx=10, bg='#ceb180').grid(row=4, column=3)

    admin_page.mainloop()