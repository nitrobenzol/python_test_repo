from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("New Gleb", "New Sarkisov", "New Igorevich", "New Moscow, Veneskaya St, 23, Apt 119", "New 4957166231",
                        "New 9866662325", "New 123123123", "New 1414141414", "New glebsarkisov@gmail.com", "New asdasdasd@com",
                        "New wdwdwdwdwdw@gmail.com"))
    app.session.logout()

def test_edit_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="New Glebss"))
    app.session.logout()