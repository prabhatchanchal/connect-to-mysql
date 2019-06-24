"""
    1. Create DataBase
    2. Create Table in Database following ORM
    3. Add mysql-connector library in your program
        > Settings > > Project > Project Interpreter
"""

import mysql.connector

class Customer:
    def __init__(self, name="NA", phone="NA", email="NA"):
        self.name = name
        self.phone = phone
        self.email = email
print("for view customer enter 1")
print("for add customer enter 2")

run1=int(input("Enter 1 or 2 : "))
c1 = Customer()
if run1==1:
    print("view customer")
    sql = "select * from customer"
    con = mysql.connector.connect(user="root", password="", host="localhost", database="harsh_python")

    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        #print(row)
        print(row)

    print(row[1], " view customer  name in DataBase")

elif run1==2:
    print("Choose an Option:")
    print("1. Add Customer")
    print("2. Update Customer")
    print("3. Delete Customer")
    print("4. View Customer")
    choice = int(input("Please Enter Your Choice: "))
    if choice == 1:
        c1.name = input("Enter Customer Name: ")
        c1.phone = input("Enter Customer Phone: ")
        c1.email = input("Enter Customer Email: ")
        sql = "insert into customer values(null, '{}', '{}', '{}')".format(c1.name, c1.phone, c1.email)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="harsh_python")

    # 3. Create cursor from connection to execute sql commands : insert/update/delete and select commands
        cursor = con.cursor()
        cursor.execute(sql)

    # 4. Commit as Transaction
        con.commit() # Transaction

        print(c1.name," Saved in DataBase")


    elif choice == 2:
        print("Update name")
        c1.name = input("Enter Customer Name: ")
        c1.phone = input("Enter Customer Phone: ")
        c1.email = input("Enter Customer Email: ")
        sql = "update customer set name={} where phone={}".format(c1.name,c1.phone)

        con = mysql.connector.connect(user="root", password="", host="localhost", database="harsh_python")

        cursor = con.cursor()
        cursor.execute(sql)


        con.commit()  # Transaction

        print(c1.name, " updated name in DataBase")

    elif choice == 3:
        print("Delete")
        c1.name = input("Enter Customer Name: ")
        c1.phone = input("Enter Customer Phone: ")
        c1.email = input("Enter Customer Email: ")
        sql = "delete from customer where phone={}".format( c1.phone)

        con = mysql.connector.connect(user="root", password="", host="localhost", database="harsh_python")

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit()  # Transaction

        print(c1.name, " updated name in DataBase")

    elif choice == 4:
        print("view customer")
        c1.name = input("Enter Customer Name: ")
        c1.phone = input("Enter Customer Phone: ")
        c1.email = input("Enter Customer Email: ")
        sql = "select * from customer where cid = {}".format(c1.cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="harsh_python")

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit()  # Transaction

        print(c1.name, " view customer  name in DataBase")
