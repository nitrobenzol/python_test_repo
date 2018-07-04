import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password, unix_socket):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.unix_socket = unix_socket
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, unix_socket=unix_socket)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home_phone, mobile_phone, work_phone, secondary_phone) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, address=address, email=email,
                                    email2=email2, email3=email3, home_phone=home_phone, work_phone=work_phone,
                                    mobile_phone=mobile_phone, secondary_phone=secondary_phone,
                                    all_emails_from_home_page=None, all_phones_from_home_page=None))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()