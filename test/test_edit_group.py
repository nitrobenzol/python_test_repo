from model.group import Group
import random


def test_edit_some_group_name(app, db, check_ui):
    group = Group(name="Some name", header="Some header", footer="Some footer")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    app.group.modify_group_by_id(random_group.id, group)
    # assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    # need to select group with same id from the list of old groups and replace with already edited group
    old_groups(????)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="Some header"))
#    old_groups = app.group.get_group_list()
#    app.group.modify(Group(header="New edited header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)