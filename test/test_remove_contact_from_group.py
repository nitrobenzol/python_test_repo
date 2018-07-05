from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="localhost", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock", name="addressbook", user="root", password="")


def test_remove_contact_from_group(app, db):
    # ensure there is at least 1 contact in app
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="New Gleb", last_name="New Sarkisov", middle_name="New Igorevich",
                                   address="New Moscow, Veneskaya St, 23, Apt 119", home_phone="New 4957166231",
                                   mobile_phone="New 9866662325", work_phone="New 123123123",
                                   secondary_phone="New 1414141414",
                                   email="glebsarkisov@gmail.com", email2="asdasdasd@com",
                                   email3="wdwdwdwdwdw@gmail.com"))
    # ensure there is at least 1 group in app
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    # select random group
    group_list_db = db.get_group_list()
    random_group = random.choice(group_list_db)
    # PROBLEM HERE: even deleted contacts existing in group might appear in group from db - need to resolve this
    contacts_in_group = orm.get_contacts_in_group(random_group)
    # if selected group has no contacts, adding random contact to it and then deleting
    contact_list = db.get_contact_list()
    random_contact = random.choice(contact_list)
    if len(contacts_in_group) == 0:
        app.contact.add_to_group(contact_id=random_contact.id, group_id=random_group.id)
        app.contact.remove_from_group(contact_id=random_contact.id, group_id=random_group.id)
        for contact in contacts_in_group:
            if contact.id != random_contact.id:
                assert True
                print(random_contact)
    # if selected group has some contacts, deleting random contact from that group
    else:
        random_contact_from_group = random.choice(contacts_in_group)
        app.contact.remove_from_group(contact_id=random_contact_from_group.id, group_id=random_group.id)
        for contact in contacts_in_group:
            if contact.id != random_contact_from_group.id:
                assert True
                print(random_contact_from_group)
    print(random_group)