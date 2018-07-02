from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creation(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creation()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_some_contact(index)
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        # submit deletion - home page will be opened right after automatically
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        # submit deletion - home page will be opened right after automatically
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//*[@id='MassCB']")) > 0):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        self.select_some_contact(0)

    def select_some_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id=')]")[index].click()
        # row = wd.find_elements_by_name("entry")[index]
        # cell = row.find_elements_by_tag_name("td")[7]
        # cell.find_element_by_tag_name("a").click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        # click Edit button
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit changes - home page will be opened right after automatically
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def edit_first_contact_via_profile(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # open profile
        self.view_first_contact_profile()
        # click modify
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact)
        # submit changes - home page will be opened right after automatically
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact_via_profile(self):
        wd = self.app.wd
        self.open_home_page()
        self.view_first_contact_profile()
        # click modify
        wd.find_element_by_name("modifiy").click()
        # click delete - home page will be opened right after automatically
        wd.find_element_by_xpath(".//input[@value='Delete']").click()
        self.contact_cache = None

    def view_first_contact_profile(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href,'view.php?id=')]").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id=')]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, address=address, email=email, email2=email2,
                       email3=email3, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone,mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)
