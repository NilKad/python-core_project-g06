import pickle

# Example: filename = 'adressbook.bin'
class AddressBook:
    pass

def handler_load(filename):
    try:
        with open(filename, "rb") as fh:
            unpacked = pickle.load(fh)
            book = unpacked
            print("Book loaded !")
    except Exception:
        book = AddressBook()
        print("Book created !")
    return book


def handler_save(book: AddressBook, filename):
    with open(filename, "wb") as fh:
        pickle.dump(book, fh)
        print('Book saved !')
