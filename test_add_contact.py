# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert()
        return True
    except:
        return False


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_login_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.open_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Tom")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Walles")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("701 First Ave, Houston, TX 77007")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+71243212555")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("tomwalles77@gmai.com")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("10")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("byear").send_keys("1992")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Tom, Houston")
        wd.find_element_by_name("submit").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_login_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
