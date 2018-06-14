from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    contact = Contact("New Gleb", "New Sarkisov", "New Igorevich", "New Moscow, Veneskaya St, 23, Apt 119", "New 4957166231",
                        "New 9866662325", "New 123123123", "New 1414141414", "New glebsarkisov@gmail.com", "New asdasdasd@com",
                        "New wdwdwdwdwdw@gmail.com")
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Jack"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_first_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Ivan"))
#    app.contact.edit_first_contact(Contact(first_name="New Glebss"))