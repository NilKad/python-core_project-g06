from datetime import datetime, timedelta
from address import Address
from birthday import Birthday
from email import Email
from FirstName import FirstName
from LastName import LastName
from record import Record
from collections import UserDict


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, first_name, last_name, address_string, email_value, birthday_date):
        contact = Record(first_name, last_name, address_string, email_value, birthday_date)
        self.contacts[(first_name, last_name)] = contact

    def nearby_birthday(self, n_days):
        now = datetime.now().timetuple().tm_yday
        future = now + int(n_days)
        new_year_future = 0

        if future > 365:
            new_year_future = future - 365
            future = 365

        fut_list = []

        for key, contact in self.contacts.items():
            birthday_date = contact.birthday_date.timetuple().tm_yday

            if birthday_date <= future and birthday_date >= now or birthday_date >= 1 and birthday_date <= new_year_future:
                fut_list.append(key)

        if fut_list:
            print(f"Following users are celebrating birthdays in the next {n_days} days:")
        else:
            print(f'No contacts are celebrating their birthday in the next {n_days} days')

        result = ", ".join(map(lambda x: " ".join(x), fut_list))
        return result

# if __name__ == "__main__":
#     address_book = AddressBook()

#     # Adding a contact
#     address_book.add_contact("John", "Doe", "123 Main St", "john.doe@example.com", datetime(1990, 2, 22))

#     # Finding nearby birthdays
#     nearby_birthdays_result = address_book.nearby_birthday(7)
#     print(nearby_birthdays_result)