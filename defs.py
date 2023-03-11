import sqlite3

class Manager():
    def __init__(self):
        self.name = " "
        self.ID = " "
        self.password = " "

class Student():
    def __init__(self):
        self.name = " "
        self.ID = " "
        self.password = " "
        self.DOB = " "
        self.standard = 0
        self.gender = " "
        self.school = " "
        self.CG = 0
        self.parentalIncome = 0
        #self.contact = Contact()

class Donor():
    def __init__(self):
        self.name = " "
        self.ID = " "
        self.password = " "
        self.plan = " "
        #self.contact = Contact()

class Admin():
    def __init__(self):
        self.name = " "
        self.ID = " "
        self.password = " "
        self.zipcode = " "
        #self.contact = Contact()

donors_db = sqlite3.connect('donors_record.db')
d_c = donors_db.cursor()
