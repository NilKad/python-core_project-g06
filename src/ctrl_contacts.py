# from contacts import birthday
# from contacts.contacts import contacts
from save_load.save_load import storage_save_file
from storage_svc import get_storage_contacts

# from main import get_storage_contacts

# from main import my_storage

# import __main__

# contacts_storage = my_storage['Contacts']
# contacts_storage_data = contacts_storage['data']
# global my_storage

# print(__main__.my_storage)

# print(get_storage_contacts())
# my_storage_conta
stor_contacts = get_storage_contacts()
# stor_data = stor_contacts["data"]
# stor_path = stor_contacts["path"]

# print("0000000000000000000000000")
# print(stor_contacts)


def contact_add(*args, **kwargs):
    params, *_ = args
    res = stor_contacts["Contacts"]["data"].add(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_find_by_id(*args, **kwargs):
    params, *_ = args
    res = stor_contacts["Contacts"]["data"].find_by_id(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_set(*args, **kwargs):
    params, *_ = args
    find_contact = stor_contacts["Contacts"]["data"].find_by_id(params)
    res = find_contact.update_all(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_phone_add(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


def contact_phone_edit(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


def contact_phone_del(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


def contact_del(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


def contact_find(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


def contact_birthday(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")
    # res = birthday(params)
    # print(f"result search birthday:\n {res}")
    # return res


def contact_showall(*args, **kwargs):
    params, *_ = args
    for_out = stor_contacts["Contacts"]["data"].data
    res = stor_contacts["Contacts"]["data"].show_all(for_out)
    # storage_save_file(stor_contacts["Contacts"])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_show(*args, **kwargs):
    params, *_ = args
    print(f"note_add args: {args}")
    print(f"note_add args: {params}")
    print(f"note_add kwargs: {kwargs}")

    return "Note edit OK"
