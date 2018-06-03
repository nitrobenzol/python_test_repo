from model.group import Group


def test_edit_first_group_name(app):

    app.group.modify(Group(name="New edited name"))

def test_edit_first_group_header(app):

    app.group.modify(Group(header="New edited header"))