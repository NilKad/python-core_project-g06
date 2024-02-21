import pickle

# Example: filename = 'adressbook.bin'


def storage_load_file_new(storage, path_str):
    filename = path_str
    # store = storage.contacts
    try:
        with open(filename, "rb") as fh:
            unpacked = pickle.load(fh)
            # book = unpacked
            storage.data = unpacked
            # storage["data"] = book
            print("Book loaded !")
    except Exception as err:
        # book = AddressBook()
        # print("Book created !")
        raise err
        # print("load_error")
    return storage


def storage_load_file(storage):
    filename = storage["path"]
    try:
        with open(filename, "rb") as fh:
            unpacked = pickle.load(fh)
            # book = unpacked
            storage["data"].data = unpacked
            print("Book loaded !")
    except Exception as err:
        # book = AddressBook()
        # print("Book created !")
        raise err
        # print("load_error")
    return storage


def storage_save_file(storage):
    stor = storage["data"].data
    filename = storage["path"]
    with open(filename, "wb") as fh:
        pickle.dump(stor, fh)
        print("Book saved !")


def storage_save_file_new(my_stor_contacts, my_stor_contacts_path):
    stor = my_stor_contacts.data
    filename = my_stor_contacts_path
    with open(filename, "wb") as fh:
        pickle.dump(stor, fh)
        print("Book saved !")
