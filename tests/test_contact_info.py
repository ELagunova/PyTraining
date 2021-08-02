from model.contact import Contact
import re
from random import randrange


def test_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", homephone="213243", workphone="5674321",
                                   mobile="+7165438555", secondaryphone="78212342", email="adamcol@gmail.com",
                                   email2="adamcol11@gmail.com", email3="adamcol22@gmail.com",
                                   bday="19", bmonth="May", byear="1998"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_like_on_home_page('email', [contact_from_edit_page.email,
                                                                                  contact_from_edit_page.email2,
                                                                                  contact_from_edit_page.email3])
    assert contact_from_home_page.all_phones_from_home_page == merge_like_on_home_page('phone',
                                                                     [contact_from_edit_page.homephone,
                                                                     contact_from_edit_page.mobile,
                                                                     contact_from_edit_page.workphone,
                                                                     contact_from_edit_page.secondaryphone])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_like_on_home_page(type, data):
    if type == 'email':
        return "\n".join(filter(lambda x: x != '',
                                    filter(lambda x: x is not None,
                                           data)))
    elif type == 'phone':
        return "\n".join(filter(lambda x: x != '',
                         map(lambda x: clear(x),
                             filter(lambda x: x is not None,
                                    data))))
