from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
