import pickle

# Example: filename = 'adressbook.bin'


def storage_load_file(storage):
    filename = storage["path"]
    try:
        with open(filename, "rb") as fh:
            unpacked = pickle.load(fh)
            storage["data"].data = unpacked["stor"]
            storage["data"].id = unpacked["id"]
    except Exception as err:
        raise err
    return storage


def storage_save_file(storage, id=None):
    filename = storage["path"]
    stor = {"id": storage.id, "stor": storage["data"]}

    with open(filename, "wb") as fh:
        pickle.dump(stor, fh)
        # print(f"Book saved {storage.__name__}!")


# def storage_save_file_new(my_stor_contacts, my_stor_contacts_path):
#     stor = my_stor_contacts.data
#     filename = my_stor_contacts_path
#     with open(filename, "wb") as fh:
#         pickle.dump(stor, fh)
#         print("Book saved !")


# def storage_load_file_new(storage, path_str):
#     filename = path_str
#     try:
#         with open(filename, "rb") as fh:
#             unpacked = pickle.load(fh)
#             storage.data = unpacked
#             print("Book loaded !")
#     except Exception as err:
#         raise err
#     return storage
