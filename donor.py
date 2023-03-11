from tkinter import *
import defs
import tkinter.messagebox as msg

def donor_reg():
    # defs.donors_db.commit()
    # defs.donors_db.close()
    if(len(fname.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(lname.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(password.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(confirm_pw.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(amount.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(ph.get())==0): return msg.showwarning('NMS says','Please fill all the entries')

    if(password.get() != confirm_pw.get()): return msg.showerror('NMS says', "Cannot confirm password")

    if(fname.get().isalpha()==0 or lname.get().isalpha==0): return msg.showerror('NMS says', "Invalid Input")

    try:
        amount_ = int(amount.get())
    except:
        return msg.showerror('NMS says', "Invalid Input")

    try:
        ph_ = int(ph.get())
    except:
        return msg.showerror('NMS says', "Invalid Input")

    msg.showinfo('NMS says', "Registration Success!"+"\n"+"Thank you for choosing us.")
    fname.delete(0,END)
    lname.delete(0,END)
    password.delete(0,END)
    confirm_pw.delete(0,END)
    amount.delete(0, END)

def reg(dreg_frame, reg_frame):
    reg_frame.grid_forget()
    dreg_frame.grid(row=3, column=1, columnspan=2)
    
    Label(dreg_frame, text="First Name: ", bg='#ceb180').grid(row=1, column=1)
    Label(dreg_frame, text="Last Name: ", bg='#ceb180').grid(row=2, column=1)
    Label(dreg_frame, text="Password: ", bg='#ceb180').grid(row=3, column=1)
    Label(dreg_frame, text="Confirm Password: ", bg='#ceb180').grid(row=4, column=1)
    Label(dreg_frame, text="Phone: ", bg='#ceb180').grid(row=5, column=1)
    Label(dreg_frame, text="Amount Intended: ", bg='#ceb180').grid(row=6, column=1)
    Label(dreg_frame, text="Plan: ", bg='#ceb180').grid(row=7, column=1)

    global fname, lname, password, confirm_pw, amount, plan, ph
    
    fname = Entry(dreg_frame)
    fname.grid(row=1, column=2)

    lname = Entry(dreg_frame)
    lname.grid(row=2, column=2)

    password = Entry(dreg_frame, show="*")
    password.grid(row=3, column=2)

    confirm_pw = Entry(dreg_frame, show="*")
    confirm_pw.grid(row=4, column=2)

    ph = Entry(dreg_frame)
    ph.grid(row=5, column=2)

    amount = Entry(dreg_frame)
    amount.grid(row=6, column=2)

    plan=StringVar()
    Radiobutton(dreg_frame, bg='#ceb180', text="Semi-Annually", variable=plan, value="Semi-Annually").grid(row=7, column=2)
    Radiobutton(dreg_frame, bg='#ceb180', text="Annually", variable=plan, value="Annually").grid(row=7, column=3)

    next_button = Button(dreg_frame, text="Register", command=donor_reg)
    next_button.grid(row=8, column=4)

def login(frame):
    
    frame.grid_forget()
    frame.grid(row=3, column=1, columnspan=4)
    
    Label(frame, text="Donor ID: ", bg='#ceb180').grid(row=1, column=1)
    Label(frame, text="Password: ", bg='#ceb180').grid(row=2, column=1)

    global id, password
    
    id = Entry(frame)
    id.grid(row=1, column=2)

    password = Entry(frame, show="*")
    password.grid(row=2, column=2)

    next_button = Button(frame, text="Log in", command=donor_login)
    next_button.grid(row=4, column=4)

def donor_login():
    if(len(id.get())==0 or len(password.get())==0):
        return msg.showerror('NMS says', "Invalid Input!")
    
    id.delete(0, END)
    password.delete(0, END)

    donor_page = Tk()
    donor_page.configure(bg='#ceb180')

    Button(donor_page, text="Logout", command=donor_page.destroy).grid(row=1, column=4)
    Label(donor_page, text=" ", padx=30, bg='#ceb180').grid(row=2, column=1)
    Label(donor_page, text=" ", padx=10, bg='#ceb180').grid(row=4, column=3)
    Button(donor_page, text="Update Plan", command=lambda: donor_update(donor_page)).grid(row=3,column=2)

    donor_page.mainloop()

def donor_update(donor_page):
    update=LabelFrame(donor_page, text="Update Plan", bg='#ceb180', padx=20)
    update.grid(row=5, column=2, columnspan=2)
    
    global newAmount
    
    Label(update, text="New Amount", bg='#ceb180').grid(row=1, column=1)
    newAmount=Entry(update)
    newAmount.grid(row=1, column=2)

    newPlan=StringVar()
    Radiobutton(update, bg='#ceb180', text="Semi-Annually", variable=newPlan, value="Semi-Annually").grid(row=2, column=2)
    Radiobutton(update, bg='#ceb180', text="Annually", variable=newPlan, value="Annually").grid(row=2, column=3)

    Button(update, text="Update", command=lambda: confirm_update(update)).grid(row=3, column=2)

def confirm_update(update_frame):
    msg.showinfo("NMS says", "Update Success!")
    update_frame.destroy()