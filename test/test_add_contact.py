from model.contact import Contact


def test_add_contact(app):
    contact = Contact("Gleb", "Sarkisov", "Igorevich", "Moscow, Veneskaya St, 23, Apt 119", "4957166231",
                        "9866662325", "123123123", "1414141414", "glebsarkisov@gmail.com", "asdasdasd@com",
                        "wdwdwdwdwdw@gmail.com")
    # get list of all contacts presented before create action - old_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    # get list of all contacts presented after create action - new_contacts
    new_contacts = app.contact.get_contacts_list()
    # add new contact to old list of contacts
    old_contacts.append(contact)
    # check if old_contacts + contact == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)