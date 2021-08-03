from sys import maxsize


class Contact:

    def __init__(self, id=None, first_name=None, last_name=None, address=None, all_phones_from_home_page=None,
                 homephone=None, workphone=None, mobile=None, secondaryphone=None, all_emails=None, email=None,
                 email2=None, email3=None, bday=None, bmonth=None, byear=None, notes=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.all_phones_from_home_page=all_phones_from_home_page
        self.homephone = homephone
        self.workphone = workphone
        self.mobile = mobile
        self.secondaryphone = secondaryphone
        self.all_emails = all_emails
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.notes = notes

    # строковое представление объекта
    def __repr__(self):
        return "%s%s%s%s" % (self.id, self.first_name, self.last_name, self.bmonth)

    # функция сравнения объектов
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.first_name == other.first_name) and \
               (self.last_name == other.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize