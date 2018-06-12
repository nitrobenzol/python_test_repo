from model.contact import Contact


def test_add_contact(app):
    contact = Contact("Gleb", "Sarkisov", "Igorevich", "Moscow, Veneskaya St, 23, Apt 119", "4957166231",
                        "9866662325", "123123123", "1414141414", "glebsarkisov@gmail.com", "asdasdasd@com",
                        "wdwdwdwdwdw@gmail.com")
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)