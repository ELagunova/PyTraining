import random

import allure

from model.contact import Contact
from model.group import Group


def check_group_contact_list(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    if len(orm.get_group_list()) == 0 or len(orm.get_not_full_group(len(orm.get_contact_list()))) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))


def add_contact_to_group(app, orm):
    check_group_contact_list(app, orm)
    groups_list = orm.get_not_full_group(len(orm.get_contact_list()))
    group = random.choice(groups_list)
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_to_group(contact, group)
    return contact, group


def test_add_contact_to_group(app, orm):
    with allure.step('Add contact to group'):
        contact, group = add_contact_to_group(app, orm)
    with allure.step('Check that contact added to group'):
        assert contact in orm.get_contacts_in_group(group)


def test_del_contact_from_group(app, orm):
    with allure.step('Given groups list that contains contacts'):
        groups_with_contacts = orm.get_groups_with_contacts()
        if len(groups_with_contacts) == 0:
            check_group_contact_list(app, orm)
            contact, group = add_contact_to_group(app, orm)
        else:
            group = random.choice(groups_with_contacts)
            contact = random.choice(orm.get_contacts_in_group(group))
    with allure.step('Delete %s from group %s' %(contact, group)):
        app.contact.delete_contact_from_group(group.id, contact.id)
    with allure.step('Check deleting operation'):
        assert contact in orm.get_contacts_not_in_group(group)
