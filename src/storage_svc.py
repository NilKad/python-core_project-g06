import os
from contacts.contacts import Contacts
from notes.notes import Notes
from save_load.save_load import storage_load_file, storage_load_file_new, storage_save_file, storage_save_file_new


my_storage = {}
my_stor_contacts = Contacts()
my_stor_contacts_path = "storage_contacts_new.bin"
my_storage_list = {Notes: "storage_notes.bin", Contacts: "storage_contacts.bin"}


# print(my_storage)


def get_storage_contacts():
    return my_storage
    pass


def storage_init(stor_class, stor_path):
    class_name = str(stor_class.__name__)
    print(f"*******    type: {class_name}")
    my_storage[class_name] = {}
    my_storage[class_name]["data"] = stor_class()
    my_storage[class_name]["path"] = stor_path
    print(f"*******    my_storage: {my_storage[class_name]["data"].__dict__}")
    # print(f"*******    my_storage: {my_storage[class_name]["data"]['contacts']}")
    
    
    
    
    
    # print(f"*******    data: {class_name['data']}")


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
        if os.path.exists(my_stor_contacts_path):
            # storage_init(stor_class, stor_path)
            try:
                storage_load_file_new(my_stor_contacts, my_stor_contacts_path )
            except Exception:
                print("!!!Error load. Save New structore")
                storage_save_file_new(my_stor_contacts, my_stor_contacts_path)
                print(type(Exception))
        else:
            # storage_init(stor_class, stor_path)
            storage_save_file_new(my_stor_contacts, my_stor_contacts_path)

