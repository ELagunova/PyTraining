from model.contact import Contact


def test_edit_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Tomas", last_name="Walless")
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

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
