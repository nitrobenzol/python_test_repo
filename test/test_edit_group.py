from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Some name"))
    app.group.modify(Group(name="New edited name"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Some header"))
    app.group.modify(Group(header="New edited header"))