# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Tom", last_name="Walles",
                               address="701 First Ave, Houston, TX 77007", mobile="+71243212555",
                               email="tomwalles77@gmai.com", bday="10", bmonth="January", byear="1992",
                               notes="Tom, Houston"))
    app.session.logout()


def test_add_contact_without_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Richard", last_name="Baket",
                               address="123 Second Ave, Houston, TX 77008", mobile="+7127431239",
                               email="", bday="17", bmonth="June", byear="1996",
                               notes="Richard, Houston"))
    app.session.logout()
