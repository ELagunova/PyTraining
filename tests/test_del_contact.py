from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    app.contact.delete_first()


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Dylan", last_name="Tomas",
                                   address="799 Green Ave, Houston, TX 94007", mobile="+7165888555",
                                   email="tomasd@gmai.com", bday="20", bmonth="June", byear="1996"))
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", mobile="+7165438555",
                                   email="adamcol@gmai.com", bday="19", bmonth="May", byear="1998"))
    app.contact.delete_all()