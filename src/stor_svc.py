import os
from contacts.contacts import Contacts
from notes.notes import Notes
from save_load.save_load import (
    storage_load_file,
    # storage_load_file_new,
    storage_save_file,
    # storage_save_file_new,
)

__structure_storage = {
    "NameAPP1": {"data": "class", "path": "string"},
    "NameAPP2": {"data": "class", "path": "string"},
    # ........
}
__structure_class = {"id": int, "data": ["record1", "record2"]}

__structure_storage_new = {
    "NameAPP1": {"box": "class", "path": "string"},
    "NameAPP2": {"box": "class", "path": "string"},
    # ........
}
__structure_class_new = {"stor": {"id": int, "data": ["record1", "record2"]}}


my_storage = {}
my_stor_contacts = Contacts()
my_stor_contacts_path = "storage_contacts_new.bin"
my_storage_list = {Notes: "storage_notes.bin", Contacts: "storage_contacts.bin"}


# print(my_storage)


def get_id_by_name(name):
    for key, path in my_storage_list.items():
        if name == key.__name__:
            id = my_storage[name]["id"]
            return [id, path]


def get_stor_contacts():
    return my_storage


def get_stor_note():
    return my_storage


def get_stor_contacts_box():
    return my_storage["Contacts"]


def get_stor_contacts_data():
    return my_storage["Contacts"].data


def get_stor_contacts_path():
    return my_storage["Contacts"].path


def get_stor_note_box():
    return my_storage["Notes"]


def get_stor_note_data():
    return my_storage["Notes"].data


def get_stor_note_path():
    return my_storage["Notes"].path


def storage_init(stor_class, stor_path):
    class_name = str(stor_class.__name__)
    my_storage[class_name] = {}
    my_storage[class_name]["data"] = stor_class()
    my_storage[class_name]["path"] = stor_path


def storage_load():
    for stor_class, stor_path in my_storage_list.items():

        if os.path.exists(stor_path):
            storage_init(stor_class, stor_path)
            try:
                storage_load_file(my_storage[stor_class.__name__])
            except Exception:
                print("!!!Error load. Save New structore")
                storage_save_file(my_storage[stor_class.__name__])
                print(type(Exception))
        else:
            storage_init(stor_class, stor_path)
            storage_save_file(my_storage[stor_class.__name__])

        # типа новая верси, тестировалась
        # if os.path.exists(my_stor_contacts_path):
        #     # storage_init(stor_class, stor_path)
        #     try:
        #         storage_load_file_new(my_stor_contacts, my_stor_contacts_path)
        #     except Exception:
        #         print("!!!Error load. Save New structore")
        #         storage_save_file_new(my_stor_contacts, my_stor_contacts_path)
        #         print(type(Exception))
        # else:
        #     # storage_init(stor_class, stor_path)
        #     storage_save_file_new(my_stor_contacts, my_stor_contacts_path)
