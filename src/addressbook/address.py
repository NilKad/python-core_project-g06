class Address:
    def __init__(self, address_string):
        self._address_string = address_string

    @property
    def address_string(self):
        return self._address_string

    @address_string.setter
    def address_string(self, new_address):
        self._address_string = new_address

    def __str__(self):
        return self.address_string