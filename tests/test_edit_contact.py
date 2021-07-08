from model.contact import Contact


def test_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(first_name="Tomas", last_name="Walless"))
    app.session.logout()


def test_edit_contacts_data(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(address="702 First Ave, Houston, TX 77027", mobile="+72243212555",
                                   email="tomaswalless77@gmail.com"))
    app.session.logout()


def test_edit_bdate(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(bday="12", bmonth="January", byear="1992"))
    app.session.logout()


def test_edit_notes(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(notes="Tom, Houston edit"))
    app.session.logout()
