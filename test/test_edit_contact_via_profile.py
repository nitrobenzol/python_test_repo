from model.contact import Contact


def test_edit_first_contact_via_profile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Someone"))
    app.contact.edit_first_contact_via_profile(Contact("Edited_Gleb", "Edited_Sarkisov", "Edited_Igorevich", "Edited_Moscow, Veneskaya St, 23, Apt 119", "Edited_4957166231",
                        "Edited_9866662325", "Edited_123123123", "Edited_1414141414", "Edited_glebsarkisov@gmail.com", "Edited_asdasdasd@com",
                        "Edited_wdwdwdwdwdw@gmail.com"))