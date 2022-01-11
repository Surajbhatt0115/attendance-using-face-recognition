import mysql.connector as msc
from datetime import date



def databasechanges():
   mydb = msc.connect( host='localhost' ,user= 'root',password = '' , port = '3306' , database = 'suraj')
   mycursor = mydb.cursor() # middle man
   c_date = date.today()

   try:
      mycursor.execute("ALTER TABLE attendance ADD  `\'%s\'` varchar(1) NOT NULL DEFAULT 'A'"%c_date)
   except:
      mycursor.execute("ALTER TABLE attendance DROP  `\'%s\'`" % c_date)
      mycursor.execute("ALTER TABLE attendance ADD  `\'%s\'` varchar(1) NOT NULL DEFAULT 'A'" % c_date)

   with open('attendance.csv', 'r+') as fin:
      mydatalist = fin.readlines()
      #print(mydatalist)
      namelist = []

      for line in mydatalist:
         entry = line.split(',')
         namelist.append((entry[0], entry[1]))


      for i in namelist:
         mycursor.execute("UPDATE attendance SET `%(in)s` = 'P' where rollno = %(rn)s",{'in':c_date,'rn':i[0]})


   mydb.commit()

   mycursor.close()
   mydb.close()
   # my db connection object


