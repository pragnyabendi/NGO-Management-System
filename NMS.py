from tkinter import *
import admin
import donor
import manager
import student

root = Tk()
root.title("NMS")
root.configure(bg='#ceb180')


def login():
    global login_page, login_frame
    login_page = Tk()
    login_page.configure(bg='#ceb180')
    login_frame = LabelFrame(login_page, text="Login", bg='#ceb180', pady=40)
    Label(login_page, text="Login as:", bg='#ceb180').grid(row=1, column=3, columnspan=2)
    Button(login_page, text = "Admin", padx=10, command = lambda: admin.login(login_frame)).grid(row=2, column=2)
    Button(login_page, text = "Donor", padx=10, command = lambda: donor.login(login_frame)).grid(row=2, column=3)
    Button(login_page, text = "Manager", padx=10, command = lambda: manager.login(login_frame)).grid(row=2, column=4)
    Button(login_page, text = "Student", padx=10, command = lambda: student.login(login_frame)).grid(row=2, column=5)

def register():
    global reg_page, reg_frame, dreg_frame
    reg_page = Tk()
    reg_page.configure(bg='#ceb180')
    dreg_frame = LabelFrame(reg_page, text="Register as Donor", bg='#ceb180', pady=40)
    reg_frame = LabelFrame(reg_page, text="Register as Student", bg='#ceb180', pady=40)
    Label(reg_page, text="Register as:", bg='#ceb180').grid(row=1, column=1, columnspan=2)
    Button(reg_page, text = "Donor", padx=10, command = lambda: donor.reg(dreg_frame, reg_frame)).grid(row=2, column=1)
    Button(reg_page, text = "Student", padx=10, command = lambda: student.reg(dreg_frame, reg_frame)).grid(row=2, column=2)


Button(root, text = "Register", padx=10, command=register).grid(row = 1, column=2)

Button(root, text = "Login", padx=10, command = login).grid(row = 1, column=3)

Label(text = "\"Welcome\"",bg='#ceb180',padx=30, pady = 40).grid(row=2, column=1)

root.mainloop()