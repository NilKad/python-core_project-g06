import pickle

# Example: filename = 'adressbook.bin'


def storage_load_file(storage):
    filename = storage["path"]
    try:
        with open(filename, "rb") as fh:
            unpacked = pickle.load(fh)
            book = unpacked
            storage["data"] = book
            print("Book loaded !")
    except Exception as err:
        # book = AddressBook()
        # print("Book created !")
        raise err
        # print("load_error")
    return storage


def storage_save_file(storage):
    stor = storage["data"]
    filename = storage["path"]
    with open(filename, "wb") as fh:
        pickle.dump(stor, fh)
        print("Book saved !")
