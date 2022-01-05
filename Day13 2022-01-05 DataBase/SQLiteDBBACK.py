from os import name
import sqlite3
from typing import Text

class DataBase:
    def __init__(self) -> None:
        self.con=sqlite3.connect("myDB.sqlite3")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee(\
                        emp_id INTEGER PRIMARY KEY AUTOINCREMENT, \
                        emp_name VARCHAR(50), \
                        email VARCHAR(50),\
                        salary MONEY)")
        self.con.commit()
    
    def insertData(self):
        print("ADD NEW RECORD..!")
        print("="*50)
        EMPname=input("Name   : ")
        EMPemail=input("Email  : ")
        EMPsalary=input("Salary : ")
        
        self.cur.execute("INSERT INTO employee(emp_name,email,salary) VALUES (?,?,?)",(EMPname,EMPemail,EMPsalary))
        self.con.commit()
    
    def showData(self):
        self.cur.execute("SELECT * FROM employee")
        print("\n\n %-5s %-20s %-20s %-10s "%("ID","Employee Name","Email Address","Salary"))
        print("-"*80)
        employees=self.cur.fetchall()
        for data in employees:
            print("%-5s %-20s %-20s %-10s "%(data[0], data[1], data[2],data[3]))
        
        print(f"Total Numbers of Records: {len(employees)}")
        
        
        
   

db=DataBase()
db.insertData()     
db.showData()