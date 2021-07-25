# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Tom", last_name="Walles",
                               address="701 First Ave, Houston, TX 77007", mobile="+71243212555",
                               email="tomwalles77@gmai.com", bday="10", bmonth="January", byear="1992",
                               notes="Tom, Houston")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_without_email(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Richard", last_name="Baket",
                               address="123 Second Ave, Houston, TX 77008", mobile="+7127431239",
                               email="", bday="17", bmonth="June", byear="1996",
                               notes="Richard, Houston")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
