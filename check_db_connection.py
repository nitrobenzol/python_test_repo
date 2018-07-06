from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id='350'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

try:
    i = db.get_contact_list()
    for item in i:
        print(item)
    print(len(i))
finally:
    pass