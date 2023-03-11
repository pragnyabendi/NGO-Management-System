from tkinter import *
import tkinter.messagebox as msg

funds_available=0
funds_required=0


def login(frame):
    
    frame.grid_forget()
    frame.grid(row=3, column=1, columnspan=4)
    
    Label(frame, text="Manager ID: ", bg='#ceb180').grid(row=1, column=1)
    Label(frame, text="Password: ", bg='#ceb180').grid(row=2, column=1)

    global id, password

    id = Entry(frame)
    id.grid(row=1, column=2)

    password = Entry(frame, show="*")
    password.grid(row=2, column=2)

    next_button = Button(frame, text="Log in", command=man_login)
    next_button.grid(row=4, column=4)

def man_login():
    if(len(id.get())==0 or len(password.get())==0):
        return msg.showerror('NMS says', "Invalid Input!")
    
    id.delete(0, END)
    password.delete(0, END)

    man_page = Tk()
    man_page.configure(bg='#ceb180')

    Button(man_page, text="Logout", command=man_page.destroy).grid(row=1, column=5)
    Label(man_page, text=" ", padx=30, bg='#ceb180').grid(row=2, column=3)
    Label(man_page, text="Funds Available: ",bg='#ceb180').grid(row=3,column=1)
    Label(man_page, text="Funds Required: ",bg='#ceb180',pady=15).grid(row=4,column=1)
    Label(man_page, text=" ", padx=30, bg='#ceb180').grid(row=6, column=3)

    avail_funds = Entry(man_page, width=10)
    avail_funds.insert(END, str(funds_available))
    avail_funds.grid(row=3, column=2)

    req_funds = Entry(man_page, width=10)
    req_funds.insert(END, str(funds_required))
    req_funds.grid(row=4, column=2)

    Button(man_page, text="Request Donors", command=request_donors).grid(row=5, column=2)

    Button(man_page, text="Initiate Help", command=initiate_help).grid(row=3, column=4)
    Button(man_page, text="Inventory", command=inventory).grid(row=4, column=4)

    man_page.mainloop()

def request_donors():
    msg.showinfo('NMS says', "Request sent!")

def initiate_help():
    msg.showinfo('NMS says', "Help Initiation Successful!")

def inventory():
    inventory=Tk()
    inventory.title("Inventory")
    inventory.configure(bg='#ceb180')

    Label(inventory, text="Books", bg='#ceb180',padx=10, pady=10).grid(row=1, column=1)
    Label(inventory, text="Class:", bg='#ceb180').grid(row=2, column=1)
    Label(inventory, text="5", bg='#ceb180').grid(row=2, column=2)
    e5 = Entry(inventory, width=3)
    e5.insert(END, 0)
    e5.grid(row=2, column=3)
    Label(inventory, text="6", bg='#ceb180').grid(row=2, column=4)
    e6 = Entry(inventory, width=3)
    e6.insert(END, 0)
    e6.grid(row=2, column=5)
    Label(inventory, text="7", bg='#ceb180').grid(row=2, column=6)
    e7 = Entry(inventory, width=3)
    e7.insert(END, 0)
    e7.grid(row=2, column=7)
    Label(inventory, text="8", bg='#ceb180').grid(row=2, column=8)
    e8 = Entry(inventory, width=3)
    e8.insert(END, 0)
    e8.grid(row=2, column=9)
    Label(inventory, text="9", bg='#ceb180').grid(row=2, column=10)
    e9 = Entry(inventory, width=3)
    e9.insert(END, 0)
    e9.grid(row=2, column=11)
    Label(inventory, text="10", bg='#ceb180').grid(row=2, column=12)
    e10 = Entry(inventory, width=3)
    e10.insert(END, 0)
    e10.grid(row=2, column=13)

    Label(inventory, text="Shoes", bg='#ceb180',padx=10, pady=10).grid(row=3, column=1)
    Label(inventory, text="Size:", bg='#ceb180').grid(row=4, column=1)
    Label(inventory, text="5", bg='#ceb180').grid(row=4, column=2)
    e15 = Entry(inventory, width=3)
    e15.insert(END, 0)
    e15.grid(row=4, column=3)
    Label(inventory, text="6", bg='#ceb180').grid(row=4, column=4)
    e16 = Entry(inventory, width=3)
    e16.insert(END, 0)
    e16.grid(row=4, column=5)
    Label(inventory, text="7", bg='#ceb180').grid(row=4, column=6)
    e17 = Entry(inventory, width=3)
    e17.insert(END, 0)
    e17.grid(row=4, column=7)
    Label(inventory, text="8", bg='#ceb180').grid(row=4, column=8)
    e18 = Entry(inventory, width=3)
    e18.insert(END, 0)
    e18.grid(row=4, column=9)

    Label(inventory, text="Socks", bg='#ceb180',padx=10, pady=10).grid(row=5, column=1)
    Label(inventory, text="Size:", bg='#ceb180').grid(row=6, column=1)
    Label(inventory, text="5", bg='#ceb180').grid(row=6, column=2)
    e25 = Entry(inventory, width=3)
    e25.insert(END, 0)
    e25.grid(row=6, column=3)
    Label(inventory, text="6", bg='#ceb180').grid(row=6, column=4)
    e26 = Entry(inventory, width=3)
    e26.insert(END, 0)
    e26.grid(row=6, column=5)
    Label(inventory, text="7", bg='#ceb180').grid(row=6, column=6)
    e27 = Entry(inventory, width=3)
    e27.insert(END, 0)
    e27.grid(row=6, column=7)
    Label(inventory, text="8", bg='#ceb180').grid(row=6, column=8)
    e28 = Entry(inventory, width=3)
    e28.insert(END, 0)
    e28.grid(row=6, column=9)

    Label(inventory, text="Uniforms", bg='#ceb180',padx=10, pady=10).grid(row=7, column=1)
    Label(inventory, text="Size:", bg='#ceb180').grid(row=8, column=1)
    Label(inventory, text="S", bg='#ceb180').grid(row=8, column=2)
    e31 = Entry(inventory, width=3)
    e31.insert(END, 0)
    e31.grid(row=8, column=3)
    Label(inventory, text="M", bg='#ceb180').grid(row=8, column=4)
    e32 = Entry(inventory, width=3)
    e32.insert(END, 0)
    e32.grid(row=8, column=5)
    Label(inventory, text="L", bg='#ceb180').grid(row=8, column=6)
    e33 = Entry(inventory, width=3)
    e33.insert(END, 0)
    e33.grid(row=8, column=7)
    Label(inventory, text="XL", bg='#ceb180').grid(row=8, column=8)
    e34 = Entry(inventory, width=3)
    e34.insert(END, 0)
    e34.grid(row=8, column=9)

    Label(inventory, text="Bags:", bg='#ceb180',padx=10, pady=10).grid(row=9, column=1)
    e40 = Entry(inventory, width=3)
    e40.insert(END, 0)
    e40.grid(row=9, column=2)

    Button(inventory, text="Update", command=update_inventory).grid(row=10, column=14)

    Label(inventory, text="   ", bg='#ceb180').grid(row=10, column=15)
    Label(inventory, text="   ", bg='#ceb180', pady=5).grid(row=11, column=15)

def update_inventory():
    return msg.showinfo('NMS says', "Stock updated successfully.")