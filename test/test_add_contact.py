from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact("Gleb", "Sarkisov", "Igorevich", "Moscow, Veneskaya St, 23, Apt 119", "4957166231",
                        "9866662325", "123123123", "1414141414", "glebsarkisov@gmail.com", "asdasdasd@com",
                        "wdwdwdwdwdw@gmail.com"))