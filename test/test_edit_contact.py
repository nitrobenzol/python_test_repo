from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("New_Gleb", "New_Sarkisov", "New_Igorevich", "New_Moscow, Veneskaya St, 23, Apt 119", "New_4957166231",
                        "New_9866662325", "New_123123123", "New_1414141414", "New_glebsarkisov@gmail.com", "New_asdasdasd@com",
                        "New_wdwdwdwdwdw@gmail.com"))
    app.session.logout()