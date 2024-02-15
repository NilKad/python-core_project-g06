from datetime import datetime, timedelta

class AddressBook:
    def __init__(self):
        self.contacts = []

class Birthday:
    @staticmethod
    def upcoming_birthdays(address_book, days):
        current_date = datetime.now()
        upcoming_date = current_date + timedelta(days=days)

        upcoming_birthdays_list = []

        for contact in address_book.contacts:
            if contact.birthday is not None:
                birthday_date = datetime(current_date.year, contact.birthday.month, contact.birthday.day)

                if current_date <= birthday_date < upcoming_date:
                    upcoming_birthdays_list.append(contact)

        return upcoming_birthdays_list