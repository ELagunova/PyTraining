from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(first_name="Tomas", last_name="Walless",
                               address="702 First Ave, Houston, TX 77027", mobile="+72243212555",
                               email="tomaswalless77@gmail.com", bday="12", bmonth="January", byear="1992",
                               notes="Tom, Houston edit"))
    app.session.logout()
