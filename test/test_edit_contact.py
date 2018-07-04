from model.contact import Contact
import random
import time


def test_edit_some_contact(app, db, check_ui):
    contact = Contact(first_name="New Gleb", last_name="New Sarkisov", middle_name="New Igorevich", address="New Moscow, Veneskaya St, 23, Apt 119", home_phone="New 4957166231",
                        mobile_phone="New 9866662325", work_phone="New 123123123", secondary_phone="New 1414141414", email="glebsarkisov@gmail.com", email2="asdasdasd@com",
                        email3="wdwdwdwdwdw@gmail.com")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(random_contact.id, contact)
    new_contacts = db.get_contact_list()
    contact.id = random_contact.id
    old_contacts.remove(random_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip())
    new_contacts = map(clean, db.get_contact_list())
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)