import re
from random import randrange
from model.contact import Contact


def test_contact_info_match(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="New Gleb", last_name="New Sarkisov", middle_name="New Igorevich",
                        address="New Moscow, Veneskaya St, 23, Apt 119", home_phone="New 4957166231",
                        mobile_phone="New 9866662325", work_phone="New 123123123", secondary_phone="New 1414141414",
                        email="glebsarkisov@gmail.com", email2="asdasdasd@com",
                        email3="wdwdwdwdwdw@gmail.com"))
    all_contacts = app.contact.get_contacts_list()
    index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# def test_phones_on_contact_view_page(app):
    # contact_from_view_page = app.contact.get_contact_from_view_page(0)
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    # assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    # assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    # assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear_for_phones(s):
    return re.sub("[() -]", "", s)


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
