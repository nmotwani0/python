import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='nikhil',passwd='1234',database="nikhil")

mycursor = mydb.cursor()

mycursor.execute("select * from student")


result1 = mycursor.fetchone()

for j in result1:
	print(j)

result = mycursor.fetchall()

for i in result:
	print(i)
