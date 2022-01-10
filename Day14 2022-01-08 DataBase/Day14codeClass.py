#===== Code from class 14.1===============
import mysql.connector
#pip install mysql-connector-python

class DataBase:
    def CreateDatabase(self,db):
        mydb=mysql.connector.connect(host="localhost",user="root", passwd="")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists "+db)
        mydb.close()
        
        
    def __init__(self,dbase) -> None:
        self.CreateDatabase(dbase)
        self.con=mysql.connector.connect(host="localhost",user="root", passwd="", database=dbase)
        se

self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee(\
            emp_id INTEGER PRIMARY KEY AUTO_INCREMENT,\
            emp_name VARCHAR(50),\
            email VARCHAR(50),\
            salary INTEGER)")
        self.con.commit()
def insertData(self):
        print("ADD NEW RECORD..!")
        print("="*50)
        EMPname=input("Name   : ")
        EMPemail=input("Email  : ")
        EMPsalary=input("Salary : ")
        
        self.cur.execute("INSERT INTO employee(emp_name,email,salary) VALUES (%s,%s,%s)",(EMPname,EMPemail,EMPsalary))
        self.con.commit()
def showData(self):
        self.cur.execute("SELECT * FROM employee")
        print("\n\n %-5s %-20s %-20s %-10s"%("ID","Employee Name","Email Address","Salary"))
        print("-"*80)
        employees=self.cur.fetchall()
        for data in employees:
            print("%-5s %-20s %-20s %-10s "%(data[0], data[1], data[2], data[3]))
        
        print(f"Total Nembers of Records: {len(employees)}")
   

db=DataBase("BITM_DB")
db.insertData()
db.showData()   
