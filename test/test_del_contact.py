from model.contact import Contact
import random
import time


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Glebus"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(5)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip())
    new_contacts = map(clean, db.get_contact_list())
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)