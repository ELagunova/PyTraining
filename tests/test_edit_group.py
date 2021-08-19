import random

import allure

from model.group import Group


def test_edit_group_name(app, db, check_ui):
    group = Group(name="Edit group name")
    with allure.step('Check precondition'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step('Choose group for editing'):
        old_groups = db.get_group_list()
        edit_group = random.choice(old_groups)
        index = old_groups.index(edit_group)
    with allure.step('Edit group %s like %s' %(edit_group, group)):
        app.group.edit_random_by_id(edit_group.id, group)
    with allure.step('Check editing'):
        new_groups = db.get_group_list()
        old_groups[index] = group
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

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