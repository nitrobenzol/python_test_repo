from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", middle_name="", address="", home_phone="",
                    mobile_phone="", work_phone="", secondary_phone="", email="", email2="",
                    email3="")] + [
    Contact(first_name=random_string("first_name", 10), last_name=random_string("last_name", 10),
            middle_name=random_string("middle_name", 10), address=random_string("address", 20),
            home_phone=random_string("home_phone", 15), mobile_phone=random_string("mobile_phone", 10),
            work_phone=random_string("work_phone", 20), secondary_phone=random_string("sec_phone", 20),
            email=random_string("email1", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
