# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("Gleb", "Sarkisov", "Igorevich", "Moscow, Veneskaya St, 23, Apt 119", "4957166231",
                        "9866662325", "123123123", "1414141414", "glebsarkisov@gmail.com", "asdasdasd@com",
                        "wdwdwdwdwdw@gmail.com"))
    app.session.logout()