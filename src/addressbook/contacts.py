from datetime import datetime, timedelta
from record import Record
from collections import UserDict
from contact import Contact
from edit_record import FirstName, LastName, Email, Phone, Birthday, Address, Record


class Contacts:
    def __init__(self):
        self.contacts = {}
        self.current_id = 1

    def add(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        address = data.get('address')
        birthday = data.get('birthday')
        email = data.get('email')
        phones = data.get('phones', [])

        contact = Record(first_name, last_name, address, email, birthday, phones, contact_id=self.current_id)
        contact_id = self.current_id
        self.current_id += 1
        self.contacts[contact_id] = contact
        return contact_id

    def delete(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            
    def find_by_id(self, contact_id):
        return self.contacts.get(contact_id)

    def find(self, value):
        result = []
        for contact_id, contact in self.contacts.items():
            if (
                value.lower() in contact.first_name.value.lower() or
                value.lower() in contact.last_name.value.lower() or
                value.lower() in contact.address.address_string.lower() or
                value.lower() in contact.email.value.lower() or
                any(value.lower() in phone.value.lower() for phone in contact.phones)
            ):
                result.append((contact_id, contact))
        return result

    def birthday(self, value):
        upcoming_birthdays_list = []

        for contact_id, contact in self.contacts.items():
            if contact.birthday:
                birthday_date = contact.birthday.value.timetuple().tm_yday

                if birthday_date == value:
                    upcoming_birthdays_list.append((contact_id, contact))

        return upcoming_birthdays_list