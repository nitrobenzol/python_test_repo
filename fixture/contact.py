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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
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
        wd = self.app.wd
        # open home page
        self.open_home_page()
        self.select_first_contact()
        # click delete button
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        # submit deletion - home page will be opened right after automatically
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//*[@id='MassCB']"))>0):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # click Edit button
        wd.find_element_by_xpath("//a[contains(@href,'edit.php?id=')]").click()
        self.fill_contact_form(contact)
        # submit changes - home page will be opened right after automatically
        wd.find_element_by_name("update").click()


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

    def delete_first_contact_via_profile(self):
        wd = self.app.wd
        self.open_home_page()
        self.view_first_contact_profile()
        # click modify
        wd.find_element_by_name("modifiy").click()
        # click delete - home page will be opened right after automatically
        wd.find_element_by_xpath(".//input[@value='Delete']").click()

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