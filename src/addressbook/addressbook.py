from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add_contact(self, name, address, birthday=None):
        self.data[name] = {'Address': address, 'Birthday': birthday}

    def get_birthday_date(self, name):
        if name in self.data and 'Birthday' in self.data[name]:
            birthday = self.data[name]['Birthday']
            return datetime.strptime(birthday, "%Y-%m-%d").date()
        return None