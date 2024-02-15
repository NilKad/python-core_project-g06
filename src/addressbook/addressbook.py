from collections import UserDict
from datetime import date

class AddressBook(UserDict):
    def add_address(self, name, address):
            self.data[name] = {'Address': address}
