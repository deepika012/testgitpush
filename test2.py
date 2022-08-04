import mysql.connector as conn
mydb = conn.connect(host = "localhost" , user = "root" , passwd = "deepika@1234")
cursor = mydb.cursor()

             #------entering data in the table---------
           # while inserting values in table if 4 columns are there all 4 values must be inserted
#s = "insert into deepika1.ineuron values(101, 'Raghav Agrawal' ,'raghav@gmail.com' , 1000)"

         ## if data type is varchar use single quotes while inserting the data
#cursor.execute(s)
#mydb.commit()
        ## fetching data

cursor.execute("select * from deepika1.ineuron")
for i in  cursor.fetchall():
    print(i)
