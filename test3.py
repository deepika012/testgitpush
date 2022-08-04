import mysql.connector as conn
mydb = conn.connect(host="localhost" , user = "root" , passwd = "deepika@1234")
cursor = mydb.cursor()

#cursor.execute("select emp_id , emp_name from deepika1.ineuron")
#for i in cursor.fetchall():
 #   print(i)

    # --------------storing the data in the list format------
cursor.execute("select emp_gmail , emp_name from deepika1.ineuron")
l =[]
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))

## UCI repository for data set