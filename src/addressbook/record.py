class Record:
    def __init__(self, first_name, last_name, address, email, birthday_date):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.birthday_date = birthday_date  # Set the birthday_date attribute

    def get_birthday_date(self):
        return self.birthday_date

    def __str__(self):
        return f"{self.first_name} {self.last_name}\nAddress: {self.address}\nEmail: {self.email}\nBirthday: {self.birthday_date}"