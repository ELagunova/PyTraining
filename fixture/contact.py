from model.contact import Contact


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
        self.change_field("mobile", contact.mobile)
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

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_contacts_param(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.open_home_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
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
                self.contact_cache.append(Contact(id=id, first_name=firstname, last_name=lastname))
        return self.contact_cache


