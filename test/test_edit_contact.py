from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    contact = Contact(first_name="New Gleb", last_name="New Sarkisov", middle_name="New Igorevich", address="New Moscow, Veneskaya St, 23, Apt 119", home_phone="New 4957166231",
                        mobile_phone="New 9866662325", work_phone="New 123123123", secondary_phone="New 1414141414", email="glebsarkisov@gmail.com", email2="asdasdasd@com",
                        email3="wdwdwdwdwdw@gmail.com")
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