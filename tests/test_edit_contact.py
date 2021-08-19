import random

import allure

from model.contact import Contact


def test_edit_name(app, db, check_ui):
    contact = Contact(first_name="Edited name", last_name="Edited lastname")
    with allure.step('Check precondition'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                       address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                       email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    with allure.step('Choose contact for editing'):
        old_contacts = db.get_contact_list()
        edit_contact = random.choice(old_contacts)
    with allure.step('Edit contact %s like %s' %(edit_contact, contact)):
        index = old_contacts.index(edit_contact)
        app.contact.edit_by_id(edit_contact.id, contact)
    with allure.step('Check editing'):
        new_contacts = db.get_contact_list()
        old_contacts[index] = contact
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

'''
TODO: параметризация теста модификации контактов
'''
# def test_edit_contacts_data(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Adam", last_name="Collins",
#                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
#                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
#    app.contact.edit_first(Contact(address="702 First Ave, Houston, TX 77027", mobile="+72243212555",
#                                   email="tomaswalless77@gmail.com"))

# def test_edit_bdate(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Adam", last_name="Collins",
#                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
#                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
#    app.contact.edit_first(Contact(bday="12", bmonth="January", byear="1992"))


# def test_edit_notes(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first_name="Adam", last_name="Collins",
#                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
#                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
#    app.contact.edit_first(Contact(notes="Tom, Houston edit"))
