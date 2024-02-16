from datetime import datetime, timedelta

class Birthday:
    def upcoming_birthdays(address_book, days):
        current_date = datetime.now().date()
        upcoming_date = current_date + timedelta(days=days)

        upcoming_birthdays_list = []

        for contact in address_book.values():
            birthday_date = contact.get_birthday_date()

            if birthday_date:
                birthday_date = birthday_date.replace(year=upcoming_date.year)

            if birthday_date == upcoming_date:
                upcoming_birthdays_list.append(contact)
                
        return upcoming_birthdays_list