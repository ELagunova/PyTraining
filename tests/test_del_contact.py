import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    contacts_list = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == contacts_list
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=Contact.id_or_max)


def test_delete_all_contacts(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Dylan", last_name="Tomas",
                                   address="799 Green Ave, Houston, TX 94007", mobile="+7165888555",
                                   email="tomasd@gmai.com", bday="20", bmonth="June", byear="1996"))
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    app.contact.delete_all()
    assert len(db.get_contact_list()) == 0
    if check_ui:
        assert app.contact.count() == 0
