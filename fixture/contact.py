from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) == 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def fill_contacts_param(self, contact):
        self.change_field("firstname", contact.first_name)
        self.change_field("lastname", contact.last_name)
        self.change_field("address", contact.address)
        self.change_field("home", contact.homephone)
        self.change_field("work", contact.workphone)
        self.change_field("mobile", contact.mobile)
        self.change_field("phone2", contact.secondaryphone)
        self.change_field("email", contact.email)
        self.change_field("bday", contact.bday)
        self.change_field("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)
        self.change_field("notes", contact.notes)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name not in ("bday", "bmonth", "byear"):
                wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contacts_param(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//*[@title='Edit']")[index].click()

    def select_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//a[@href = 'edit.php?id=%s']" %id).click()

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_edit_by_index(index)
        self.fill_contacts_param(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_edit_by_id(id)
        self.fill_contacts_param(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.open_home_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, first_name=firstname, last_name=lastname, address=address,
                                                  all_emails=all_emails, all_phones_from_home_page=all_phones))
        return self.contact_cache

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.select_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, first_name=firstname, last_name=lastname, address=address, email=email, email2=email2,
                       email3=email3, homephone=homephone, workphone=workphone,
                       mobile=mobile, secondaryphone=secondaryphone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile,
                       workphone=workphone, secondaryphone=secondaryphone)

