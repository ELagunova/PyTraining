# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    contact = json_contacts
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)
