from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Some name"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(name="New edited name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Some header"))
    old_groups = app.group.get_group_list()
    app.group.modify(Group(header="New edited header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)