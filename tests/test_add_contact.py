# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

MonthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}


def random_string(prefix='', maxlen=1, postfix=''):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


def random_month():
    num_month = random.randrange(1, 13, 1)
    return MonthDict[num_month]


def random_phone(maxlen):
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(5, maxlen, 1))])


testdata = [Contact(first_name=random_string('name', 5), last_name=random_string(maxlen=10),
                    address=random_string(maxlen=15), email=random_string(maxlen=10, postfix='@mail.com'),
                    mobile=random_phone(12), bday=random.randrange(30), bmonth=random_month(),
                    byear=random.randrange(1940, 2021, 1), notes=random_string(maxlen=20))
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
