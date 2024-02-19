import re


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
