from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contacts_param(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contacts_param(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//*[@title='Edit']").click()
        self.fill_contacts_param(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def delete_all(self):
        wd = self.app.wd
        self.open_home_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
