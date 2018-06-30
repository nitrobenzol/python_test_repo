import pymysql


connection = pymysql.connect(host="localhost", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
