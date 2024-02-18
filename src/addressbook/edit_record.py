from collections import UserDict

#1st variant:
class AddressBook(UserDict):
    def edit_record(self, record, old_value, new_value):
        if old_value in record:
            record[old_value] = new_value
        else:
            raise ValueError(f"{old_value} not found in the record")


#2nd variant:
#records is a list of records
class AddressBook:
    def edit_record(self, records, identifier, identifier_value, old_value, new_value):
        for record in records:
            if record.get(identifier) == identifier_value:
                if old_value in record:
                    record[old_value] = new_value
                else:
                    raise ValueError(f"{old_value} not found in the record")
        else:
            raise ValueError(f"{identifier_value} not found in the address book")