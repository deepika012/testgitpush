import mysql.connector as conn
mydb  = conn.connect(host="localhost",user = "root" ,passwd = "deepika@1234")
#print(mydb)

cursor = mydb.cursor()
#---------------fetching already stored database----------------

#cursor.execute("show databases")
#print(cursor.fetchall())

#----------------creating database------------

#cursor.execute("create database deepika12")
#cursor.execute("show databases")
#print(cursor.fetchall())

#--------creating table in database---------

#cursor.execute("create table deepika12.ineuron (emp_id int(10), emp_name varchar(80), emp_gmail varchar(20), emp_sal int(6))")
#print(cursor.execute("select * from deepika1.ineuron"))



