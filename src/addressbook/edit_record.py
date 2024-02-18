from collections import UserDict


class AddressBook(UserDict):

    def set_first_name(self, id, value):
        if id in self.data:
            self.data[id]['first_name'] = value
        else:
            raise KeyError(f'Record with id {id} not found')

    def set_last_name(self, id, value):
        if id in self.data:
            self.data[id]['last_name'] = value
        else:
            raise KeyError(f'Record with id {id} not found')

    def set_birthday(self, id, value):
        if id in self.data:
            self.data[id]['birthday'] = value
        else:
            raise KeyError(f'Record with id {id} not found')

    def set_address(self, id, value):
        if id in self.data:
            self.data[id]['address'] = value
        else:
            raise KeyError(f'Record with id {id} not found')

    def set_email(self, id, value):
        if id in self.data:
            self.data[id]['email'] = value
        else:
            raise KeyError(f'Record with id {id} not found')

    def edit_phone(self, id, old_phone, new_phone):
        if id in self.data:
            if old_phone in self.data['id']['phones']:
                self.data['id']['phones'].remove(old_phone)
                self.data['id']['phones'].add(new_phone)
            else:
                raise ValueError(f'Phone number {old_phone} not found in the record with id {id}')
        else:
            raise KeyError(f'Record with id {id} not found')
