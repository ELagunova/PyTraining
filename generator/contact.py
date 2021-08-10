from model.contact import Contact
import random
import string
import os
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == "-f":
        f = a


MonthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}


def random_string(prefix='', maxlen=1, postfix=''):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


def random_month():
    num_month = random.randrange(1, 13, 1)
    return MonthDict[num_month]


def random_phone(maxlen):
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(5, maxlen, 1))])


testdata = [Contact(first_name=random_string('name', 5), last_name=random_string(maxlen=10),
                    address=random_string(maxlen=15), email=random_string(maxlen=10, postfix='@mail.com'),
                    mobile=random_phone(12), bday=random.randrange(30), bmonth=random_month(),
                    byear=random.randrange(1940, 2021, 1), notes=random_string(maxlen=20))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
