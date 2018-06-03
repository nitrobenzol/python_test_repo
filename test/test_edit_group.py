from model.group import Group


def test_edit_first_group_name(app):

    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="New edited name"))
    app.session.logout()


def test_edit_first_group_header(app):

    app.session.login(username="admin", password="secret")
    app.group.modify(Group(header="New edited header"))
    app.session.logout()