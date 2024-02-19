import re
from datetime import datetime, timedelta


class FirstName:

    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[a-zA-Zа-яА-Я]{2,}', value):
            return False
        if not value.istitle():
            return False
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.value = value


class LastName:

    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[a-zA-Zа-яА-Я]{2,}', value):
            return False
        if not value.istitle():
            return False
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.value = value


class Email:
        
    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', value):
            return False
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.value = value


class Phone:

    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[\d-]+', value):
            raise ValueError('Invalid phone number format')
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.value = value


class Birthday:
    
    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError as e:
            raise ValueError(f"Wrong date format: {e}")

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.value = value

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


class Address:
    def __init__(self, address_string):
        self.address_str = address_string

    @property
    def address_string(self):
        return self.address_str

    @address_string.setter
    def address_string(self, new_address):
        self.address_str = new_address

    def __str__(self):
        return self.address_str


class Record:
    def __init__(self, first_name, last_name, birthday=None, address=None, email=None):
        self.first_name = FirstName(first_name)
        self.last_name = LastName(last_name)
        self.birthday = Birthday(birthday) if birthday else None
        self.address = Address(address) if address else None
        self.email = Email(email) if email else None
        self.phones = []

    def add_phone(self, phone):
        new_number = Phone(phone)
        self.phones.append(new_number)

    def remove_phone(self, phone):
        phones_to_remove = filter(lambda p: p.value == phone, self.phones)
        self.phones.remove(list(phones_to_remove)[0])

    def edit_phone(self, old_number, new_number):
        if not Phone().is_valid(new_number):
            raise ValueError('Invalid phone number format')
        found = False
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                found = True
                break

        if not found:
            raise ValueError(
                f"Phone number '{old_number}' not found in the record."
                )
     
    def set_email(self, email):
        if not Email(email).is_valid(email):
            raise ValueError('Invalid email format')
        self.email = Email(email)

    def __str__(self):
        return (
            f"Contact name: {self.first_name.value} {self.last_name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}, "
            f"Birthday: {self.birthday}, Email: {self.email}, Address: {self.address}"
        )
    

record = Record('John', 'Smith', '1987-01-23', '123 Main St', 'johnsmith@gmail.com')
record.add_phone('123-456-7890')
record.add_phone('555-456-7783')
print(record)