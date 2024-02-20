from datetime import datetime, timedelta
import re

class FirstName:
    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return re.fullmatch(r'[a-zA-Zа-яА-Я]{2,}', value) and value.istitle()

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
        return re.fullmatch(r'[a-zA-Zа-яА-Я]{2,}', value) and value.istitle()

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
        return re.fullmatch(r'[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', value)

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
        return re.fullmatch(r'[\d-]+', value)

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

class Contact:
    def set_first_name(self, value):
        self.first_name = FirstName(value)

    def set_last_name(self, value):
        self.last_name = LastName(value)

    def set_birthday(self, value):
        self.birthday = Birthday(value)

    def set_address(self, value):
        self.address = Address(value)

    def set_email(self, value):
        self.email = Email(value)

    def add_phones(self, phones):
        self.phones = [Phone(phone) for phone in phones]

    def edit_phone(self, old_phone, new_phone):
        if any(old_phone == phone.value for phone in self.phones):
            self.phones = [Phone(new_phone) if phone.value == old_phone else phone for phone in self.phones]

    def del_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def get_birthday_date(self):
        return self.birthday.value if self.birthday else None

    def edit_first_name(self, new_first_name):
        self.first_name.set_value(new_first_name)

    def edit_last_name(self, new_last_name):
        self.last_name.set_value(new_last_name)

    def edit_birthday(self, new_birthday):
        if new_birthday is not None and not Birthday(new_birthday).is_valid(new_birthday):
            raise ValueError("Invalid birthday format")
        self.birthday.set_value(new_birthday)

    def edit_address(self, new_address):
        self.address.address_string = new_address

    def edit_email(self, new_email):
        if new_email is not None and not Email(new_email).is_valid(new_email):
            raise ValueError('Invalid email format')
        self.email.set_value(new_email)

class Record:
    def __init__(self, first_name, last_name, birthday=None, address=None, email=None):
        self.first_name = FirstName(first_name)
        self.last_name = LastName(last_name)
        self.birthday = Birthday(birthday) if birthday else None
        self.address = Address(address) if address else None
        self.email = Email(email) if email else None
        self.phones = []
        self.contact_id = [1]

    def add_phone(self, phone):
        self.phones = [Phone(p) for p in phone]

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_number, new_number):
        if any(old_number == phone.value for phone in self.phones):
            self.phones = [Phone(new_number) if phone.value == old_number else phone for phone in self.phones]

    def set_email(self, email):
        self.email = Email(email)

    def __str__(self):
        return (
            f"Contact name: {self.first_name.value} {self.last_name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}, "
            f"Birthday: {self.birthday}, Email: {self.email}, Address: {self.address}"
        )