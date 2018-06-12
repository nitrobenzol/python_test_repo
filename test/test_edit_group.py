from model.group import Group


def test_edit_first_group_name(app):
    group = Group(name="Some name")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert old_groups == new_groups


#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="Some header"))
#    old_groups = app.group.get_group_list()
#    app.group.modify(Group(header="New edited header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)