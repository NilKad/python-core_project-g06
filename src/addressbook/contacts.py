from datetime import datetime, timedelta
from contact import Record
from collections import UserDict
from contact import Contact
from contact import FirstName, LastName, Email, Phone, Birthday, Address, Record

class Contacts:
    def __init__(self):
        self.contacts = {}
        self.current_id = 1

    def add(self, data):
        contact_id = self.current_id
        self.current_id += 1

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        address = data.get('address')
        birthday = data.get('birthday')
        email = data.get('email')
        phones = data.get('phones', [])

        contact = Record(first_name, last_name, address, email, birthday, phones, contact_id=contact_id)
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
                any(value in phone.value for phone in contact.phones)
            ):
                result.append((contact_id, contact))
        return result

    def birthday(self, *dates):
        upcoming_birthdays_list = []

        if not dates:
            # Scenario 1: No parameters provided
            today_date = datetime.now().date().timetuple().tm_yday
            upcoming_birthdays_list.extend(
                (contact_id, contact)
                for contact_id, contact in self.contacts.items()
                if contact.birthday and contact.birthday.value.timetuple().tm_yday == today_date
            )
        else:
            for date in dates:
                if isinstance(date, datetime):
                    # Scenario 2: Single date provided
                    day_of_year = date.date().timetuple().tm_yday
                    upcoming_birthdays_list.extend(
                        (contact_id, contact)
                        for contact_id, contact in self.contacts.items()
                        if contact.birthday and contact.birthday.value.timetuple().tm_yday == day_of_year
                    )
                elif isinstance(date, tuple) and len(date) == 2 and isinstance(date[0], datetime) and isinstance(date[1], datetime):
                    # Scenario 3: Two dates provided
                    start_date, end_date = date
                    upcoming_birthdays_list.extend(
                        (contact_id, contact)
                        for contact_id, contact in self.contacts.items()
                        if contact.birthday and start_date.date().timetuple().tm_yday <= contact.birthday.value.timetuple().tm_yday <= end_date.date().timetuple().tm_yday
                    )
        return upcoming_birthdays_list