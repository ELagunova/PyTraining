import allure

from model.contact import Contact
import re


def test_phones_on_home_page(app):
    with allure.step('Check precondition'):
        if app.contact.count() == 0:
            app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                       address="781 Green Ave, Houston, TX 94007", homephone="213243", workphone="5674321",
                                       mobile="+7165438555", secondaryphone="78212342", email="adamcol@gmail.com",
                                       bday="19", bmonth="May", byear="1998"))
    with allure.step('Given information about contacts phone from home page'):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with allure.step('Given information about contacts phone from edit page'):
        contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    with allure.step('Check that information from home page is equal to information from edit page'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    with allure.step('Check precondition'):
        if app.contact.count() == 0:
            app.contact.create(Contact(first_name="Adam", last_name="Collins",
                                       address="781 Green Ave, Houston, TX 94007", homephone="213243", workphone="5674321",
                                       mobile="+7165438555", secondaryphone="78212342", email="adamcol@gmail.com",
                                       bday="19", bmonth="May", byear="1998"))
    with allure.step('Given information about contacts phone from contact view page'):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
    with allure.step('Given information about contacts phone from edit page'):
        contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    with allure.step('Check that information from contact view page is equal to information from edit page'):
        assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))
