import mysql.connector as conn
mydb = conn.connect(host="localhost" , user = "root" , passwd = "deepika@1234")
cursor = mydb.cursor()

#cursor.execute("show databases")
#print(cursor.fetchall())
print(cursor.execute("select * from ineuron.bank_details"))


