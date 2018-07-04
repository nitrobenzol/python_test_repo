from model.contact import Contact


def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list()

    def clean(contact):
        return Contact(id=contact.id, last_name=contact.last_name.strip(), first_name=contact.first_name.strip(),
                       address=contact.address.strip(), email=contact.email.strip(), email2=contact.email2.strip(),
                       email3=contact.email3.strip(), home_phone=contact.home_phone.strip(),
                       mobile_phone=contact.mobile_phone.strip(), work_phone=contact.work_phone.strip(),
                       secondary_phone=contact.secondary_phone.strip()
                       )
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)