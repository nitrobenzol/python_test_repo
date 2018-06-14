from model.group import Group
from random import randrange


def test_edit_some_group_name(app):
    group = Group(name="Some name")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="Some header"))
#    old_groups = app.group.get_group_list()
#    app.group.modify(Group(header="New edited header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)