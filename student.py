from tkinter import *
from tkinter import messagebox as msg

def reg(dreg_frame, reg_frame):
    dreg_frame.grid_forget()
    reg_frame.grid(row=3, column=1, columnspan=2)
    
    Label(reg_frame, text="First Name: ", bg='#ceb180').grid(row=1, column=1)
    Label(reg_frame, text="Last Name: ", bg='#ceb180').grid(row=2, column=1)
    Label(reg_frame, text="Password: ", bg='#ceb180').grid(row=3, column=1)
    Label(reg_frame, text="Confirm Password: ", bg='#ceb180').grid(row=4, column=1)
    Label(reg_frame, text="DOB(DDMMYYYY): ", bg='#ceb180').grid(row=5, column=1)
    Label(reg_frame, text="Gender(M/F/O): ", bg='#ceb180').grid(row=6, column=1)
    Label(reg_frame, text="School: ", bg='#ceb180').grid(row=7, column=1)
    Label(reg_frame, text="Standard: ", bg='#ceb180').grid(row=8, column=1)
    Label(reg_frame, text="CG: ", bg='#ceb180').grid(row=9, column=1)
    Label(reg_frame, text="Parental Income: ", bg='#ceb180').grid(row=10, column=1)
    Label(reg_frame, text="Phone: ", bg='#ceb180').grid(row=11, column=1)

    global fname, lname, password, confirm_pw, dob, gender, school, std, cg, income, ph
    
    fname = Entry(reg_frame)
    fname.grid(row=1, column=2)

    lname = Entry(reg_frame)
    lname.grid(row=2, column=2)

    password = Entry(reg_frame, show="*")
    password.grid(row=3, column=2)

    confirm_pw = Entry(reg_frame, show="*")
    confirm_pw.grid(row=4, column=2)

    dob = Entry(reg_frame)
    dob.grid(row=5, column=2)

    gender = Entry(reg_frame)
    gender.grid(row=6, column=2)

    school = Entry(reg_frame)
    school.grid(row=7, column=2)

    std = Entry(reg_frame)
    std.grid(row=8, column=2)

    cg = Entry(reg_frame)
    cg.grid(row=9, column=2)

    income = Entry(reg_frame)
    income.grid(row=10, column=2)

    ph = Entry(reg_frame)
    ph.grid(row=11,column=2)

    next_button = Button(reg_frame, text="Register", command=stu_reg)
    next_button.grid(row=12, column=4)

def stu_reg():

    if(len(fname.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(lname.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(password.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(confirm_pw.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(dob.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(gender.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(school.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(std.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(cg.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(income.get())==0): return msg.showwarning('NMS says','Please fill all the entries')
    if(len(ph.get())==0): return msg.showwarning('NMS says','Please fill all the entries')

    if(password.get() != confirm_pw.get()): return msg.showerror('NMS says', "Cannot confirm password")

    if(fname.get().isalpha()==0 or lname.get().isalpha==0): return msg.showerror('NMS says', "Invalid Input")

    msg.showinfo('NMS says', "Data Saved!"+"\n"+"Our Admin will soon reach you for registration approval.")
    fname.delete(0,END)
    lname.delete(0,END)
    password.delete(0,END)
    confirm_pw.delete(0,END)
    school.delete(0,END)
    gender.delete(0,END)
    dob.delete(0,END)
    cg.delete(0,END)
    income.delete(0,END)
    std.delete(0,END)
    

def login(frame):
    
    frame.grid_forget()
    frame.grid(row=3, column=1, columnspan=4)
    
    Label(frame, text="Student ID: ", bg='#ceb180').grid(row=1, column=1)
    Label(frame, text="Password: ", bg='#ceb180').grid(row=2, column=1)

    global id, password
    
    id = Entry(frame)
    id.grid(row=1, column=2)

    password = Entry(frame, show="*")
    password.grid(row=2, column=2)

    next_button = Button(frame, text="Log in", command=stu_login)
    next_button.grid(row=4, column=4)

def stu_login():
    if(len(id.get())==0 or len(password.get())==0):
        return msg.showerror('NMS says', "Invalid Input!")
    
    id.delete(0, END)
    password.delete(0, END)

    stu_page = Tk()
    stu_page.configure(bg='#ceb180')

    Button(stu_page, text="Logout", command=stu_page.destroy).grid(row=1, column=4)
    Label(stu_page, text=" ", padx=30, bg='#ceb180').grid(row=2, column=1)
    Label(stu_page, text=" ", padx=10, bg='#ceb180').grid(row=4, column=3)
    Button(stu_page, text="Update Records", command=lambda: stu_update(stu_page)).grid(row=3,column=2)

    stu_page.mainloop()

def stu_update(stu_page):
    update=LabelFrame(stu_page, text="Update Records",bg='#ceb180', padx=20)
    update.grid(row=5, column=2, columnspan=2)
    
    global newCG, newStd, newIncome
    
    Label(update, text="Current CG", bg='#ceb180').grid(row=1, column=1)
    newCG=Entry(update)
    newCG.grid(row=1, column=2)

    Label(update, text="Current Standard", bg='#ceb180').grid(row=2, column=1)
    newStd=Entry(update)
    newStd.grid(row=2, column=2)
    
    Label(update, text="Current Parental Income", bg='#ceb180').grid(row=3, column=1)
    newIncome=Entry(update)
    newIncome.grid(row=3, column=2)

    Button(update, text="Update", command=lambda: confirm_update(update)).grid(row=6, column=2)

def confirm_update(update_frame):
    if(len(newCG.get())==0 and len(newStd.get())==0 and len(newIncome.get())==0):
        msg.showwarning('NMS says', "No data updated.")
    else: msg.showinfo("NMS says", "Data Saved!"+"\n"+"Our Admin will soon reach you for update approval.")
    update_frame.destroy()