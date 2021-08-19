import allure

from model.contact import Contact
import re
from random import randrange


def test_contact_info_from_ui_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                   address="781 Green Ave, Houston, TX 94007", homephone="213243", workphone="5674321",
                                   mobile="+7165438555", secondaryphone="78212342", email="adamcol@gmail.com",
                                   email2="adamcol11@gmail.com", email3="adamcol22@gmail.com",
                                   bday="19", bmonth="May", byear="1998"))
    with allure.step('Given a contacts list from browser'):
        contact_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Given a contacts list from database'):
        contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Check that list from browser is equal to list from database'):
        assert len(contact_from_ui) == len(contacts_from_db)
        for item in range(len(contacts_from_db)):
            assert contact_from_ui[item].first_name == contacts_from_db[item].first_name
            assert contact_from_ui[item].last_name == contacts_from_db[item].last_name
            assert contact_from_ui[item].address == contacts_from_db[item].address
            assert contact_from_ui[item].all_emails == merge_like_on_home_page('email', [contacts_from_db[item].email,
                                                                                     contacts_from_db[item].email2,
                                                                                     contacts_from_db[item].email3])
            assert contact_from_ui[item].all_phones_from_home_page == merge_like_on_home_page('phone',
                                                                                          [contacts_from_db[item].homephone,
                                                                                           contacts_from_db[item].mobile,
                                                                                           contacts_from_db[item].workphone,
                                                                                           contacts_from_db[item].secondaryphone])


def test_contact_info_on_home_page(app):
    with allure.step('Check precondition'):
        if app.contact.count() == 0:
            app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                       address="781 Green Ave, Houston, TX 94007", homephone="213243", workphone="5674321",
                                       mobile="+7165438555", secondaryphone="78212342", email="adamcol@gmail.com",
                                       email2="adamcol11@gmail.com", email3="adamcol22@gmail.com",
                                       bday="19", bmonth="May", byear="1998"))
    with allure.step('Choose random contact'):
        index = randrange(app.contact.count())
    with allure.step('Given information about contact from home page'):
        contact_from_home_page = app.contact.get_contact_list()[index]
    with allure.step('Given information about contact from edit page'):
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    with allure.step('Check that information from home page is equal to information from edit page'):
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
