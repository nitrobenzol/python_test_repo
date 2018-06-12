from model.contact import Contact


def test_edit_first_contact_via_profile(app):
    contact = Contact("Edited_Gleb", "Edited_Sarkisov", "Edited_Igorevich", "Edited_Moscow, Veneskaya St, 23, Apt 119", "Edited_4957166231",
                        "Edited_9866662325", "Edited_123123123", "Edited_1414141414", "Edited_glebsarkisov@gmail.com", "Edited_asdasdasd@com",
                        "Edited_wdwdwdwdwdw@gmail.com")
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Someone"))
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact_via_profile(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)