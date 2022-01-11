import attendance as attsy
import datab as db
import mysql.connector as msc
import pandas as pd

print("\n\t\t\t\tATTENDANCE SYSTEM\n")

while True:
    move = int(input("\n1-Mark attendance\n2-Show the attendance from database\n3-Exit\nInput Choice - "))

    if move == 1:
       attsy.face_project()
       print("\n Attendance  marked  sucessfully..!!\n")
       db.databasechanges()

    elif move == 2:
        mydb = msc.connect(host='localhost', user='root', password='', port='3306', database='suraj')
        mycursor = mydb.cursor()
        detail = pd.read_sql_query("select * from attendance", mydb)
        print("\n",detail)

    else:
        print("Exiting....the System!!")
        exit(0)