from random import randrange

from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edit group name")
    group.id = old_groups[index].id
    app.group.edit_random_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
TODO: параметризация теста модификации групп
'''
# def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header="123"))
#    app.group.edit_first(Group(header="Edit header name"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_group_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", footer="456"))
#    app.group.edit_first(Group(footer="Edit footer name"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)