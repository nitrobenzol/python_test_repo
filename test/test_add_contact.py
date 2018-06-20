from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", middle_name="", address="", home_phone="",
                    mobile_phone="", work_phone="", secondary_phone="", email="", email2="",
                    email3="")] + [
    Contact(first_name=random_string("first_name", 10), last_name=random_string("last_name", 10),
            middle_name=random_string("middle_name", 10), address=random_string("address", 20),
            home_phone=random_string("home_phone", 15), mobile_phone=random_string("mobile_phone", 10),
            work_phone=random_string("work_phone", 20), secondary_phone=random_string("sec_phone", 20),
            email=random_string("email1", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
