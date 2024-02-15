from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add_address(self, name, address):
        self.data[name] = {'Address': address}

    def get_birthday_date(self):
        if self.birthday:
            return datetime.strptime(self.birthday, "%Y-%m-%d").date()
        return None