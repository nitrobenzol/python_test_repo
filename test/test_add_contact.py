from model.contact import Contact


def test_add_contact(app):
    contact = Contact(first_name="Gleb", last_name="Sarkisov", middle_name="Igorevich", address="Moscow, Veneskaya St, 23, Apt 119", home_phone="4957166231",
                        mobile_phone="9866662325", work_phone="123123123", secondary_phone="1414141414", email="glebsarkisov@gmail.com", email2="asdasdasd@com",
                        email3="wdwdwdwdwdw@gmail.com")
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
