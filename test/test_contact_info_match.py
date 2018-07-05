import re
from model.contact import Contact


def test_contact_info_match(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(first_name="New Gleb", last_name="New Sarkisov", middle_name="New Igorevich",
                        address="New Moscow, Veneskaya St, 23, Apt 119", home_phone="New 4957166231",
                        mobile_phone="New 9866662325", work_phone="New 123123123", secondary_phone="New 1414141414",
                        email="glebsarkisov@gmail.com", email2="asdasdasd@com",
                        email3="wdwdwdwdwdw@gmail.com"))
    db_list = db.get_contact_list()
    # applying sorting by id for both lists (ui&db) so that we have equal order of contacts
    # and we will be able to use index for comparison
    sorted_db_list = sorted(db_list, key=Contact.id_or_max)
    ui_list = app.contact.get_contacts_list()
    list_length = len(ui_list)
    sorted_ui_list = sorted(ui_list, key=Contact.id_or_max)
    # loop for element with each index in the list
    for index in range(0, list_length):
        assert sorted_ui_list[index].last_name == sorted_db_list[index].last_name
        assert sorted_ui_list[index].first_name == sorted_db_list[index].first_name
        assert sorted_ui_list[index].address == sorted_db_list[index].address
        assert sorted_ui_list[index].all_emails_from_home_page == merge_emails_like_on_home_page(sorted_db_list[index])
        assert sorted_ui_list[index].all_phones_from_home_page == merge_phones_like_on_home_page(sorted_db_list[index])


def clear_for_phones(s):
    return re.sub("[() -.]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))


# function for removing inappropriate spaces which can be added by user to email,
# but which are not visible from contacts list
def clear_for_emails(s):
    return re.sub("^\s*", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_for_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
