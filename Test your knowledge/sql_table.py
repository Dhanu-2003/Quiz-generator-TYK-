import mysql.connector as msc

myconn = msc.connect(host = '127.0.0.1',port = 3306,user='root',password='Dhanu@2003')

cursor = myconn.cursor()

try:
    cursor.execute("create database TMK")
except:
    cursor.execute("use TMK")
myconn.commit()



cursor.execute("create table stu_rank(mail_id varchar(100),subject varchar(100),percentage varchar(4))")

myconn.commit()

try:
    cursor.execute("create table solved(mail_id varchar(100),subject varchar(100),question varchar(100),option varchar(100),opted varchar(2),answer varchar(2))")
except:
    print("Table Exixts")

try:
    cursor.execute("create table history(mail_id varchar(100),subject varchar(100),data1 varchar(100))")
except:
    print("Table Exixts")

""" query = cursor.execute("insert into solved values('{}','{}','{}','{}','{}','{}')".format('1','addf','questions_list[i]','.join(opt_list[i])','a','a'))
cursor.execute(query)
myconn.commit()


cursor.execute("select subject from history;")
dta = cursor.fetchall()
print(list(dta))
 """

myconn.commit()
