# -*- coding: utf-8 -*-
import allure

from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Given a contact list '):
        old_contacts = db.get_contact_list()
    with allure.step('When I add a contact %s to the list' % contact):
        app.contact.create(contact)
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)
