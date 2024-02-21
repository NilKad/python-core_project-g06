import re


class Last_name:
    def __init__(self, value):
        self.set_value(value)

    def is_valid(self, value):
        return re.fullmatch(r"[a-zA-Zа-яА-Я]{2,}", value)

    def set_value(self, value):
        if value:
            if not self.is_valid(value):
                raise ValueError("Invalid value")
        self.value = value

    def __str__(self):
        return str(self.value)
