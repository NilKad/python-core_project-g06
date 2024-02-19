class Contact:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birthday = None
        self.address = None
        self.email = None
        self.phones = []

    def set_first_name(self, value):
        self.first_name = value

    def set_last_name(self, value):
        self.last_name = value

    def set_birthday(self, value):
        self.birthday = value

    def set_address(self, value):
        self.address = value

    def set_email(self, value):
        self.email = value

    def add_phones(self, phones):
        self.phones.extend(phones)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
