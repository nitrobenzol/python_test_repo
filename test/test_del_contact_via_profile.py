from model.contact import Contact


def test_del_first_contact_via_profile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Someone"))
    app.contact.delete_first_contact_via_profile()