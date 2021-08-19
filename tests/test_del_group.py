import random

import allure

from model.group import Group


def test_delete_some_group(app, db, check_ui):
    with allure.step('Check precondition'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step('Choose group for deleting'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step('Delete %s' % group):
        app.group.delete_group_by_id(group.id)
    with allure.step('Check that group has been deleted'):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
