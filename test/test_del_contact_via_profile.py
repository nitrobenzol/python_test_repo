def test_del_first_contact_via_profile(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_via_profile()
    app.session.logout()