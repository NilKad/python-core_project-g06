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