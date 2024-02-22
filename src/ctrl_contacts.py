# from contacts import birthday
# from contacts.contacts import contacts
from save_load.save_load import storage_save_file
from stor_svc import (
    get_stor_contacts,
    get_stor_contacts_box,
    get_stor_contacts_data,
    get_stor_contacts_path,
    get_stor_note_box,
    get_stor_note_data,
    get_stor_note_path,
)


# from main import my_storage
# from save_load.save_load import storage_save_file


stor_contacts = get_stor_contacts()


stor_contacts_box = get_stor_contacts_box
stor_contacts_data = get_stor_contacts_data
stor_contacts_path = get_stor_contacts_path


def contact_add(*args, **kwargs):

    params, *_ = args
    res = stor_contacts["Contacts"]["data"].add(params)
    storage_save_file(stor_contacts["Contacts"])
    # stor_contacts["Contacts"]["data"].show_all([res])
    stor_contacts["Contacts"]["data"].show_col([res])
    
    return res


def contact_find_by_id(*args, **kwargs):
    params, *_ = args
    res = stor_contacts["Contacts"]["data"].find_by_id(params)
    # stor_contacts["Contacts"]["data"].show_all([res])
    stor_contacts["Contacts"]["data"].show_col([res])

    return res


def contact_set(*args, **kwargs):
    params, *_ = args
    find_contact = stor_contacts["Contacts"]["data"].find_by_id(params)
    res = find_contact.update_all(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_col([res])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_phone_add(*args, **kwargs):
    params, *_ = args
    find_contact = stor_contacts["Contacts"]["data"].find_by_id(params)
    res = find_contact.add_phones(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_col([res])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_phone_edit(*args, **kwargs):
    params, *_ = args
    # print(f"contact_add args: {params}")
    find_contact = stor_contacts["Contacts"]["data"].find_by_id(params)
    res = find_contact.edit_phone(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_col([res])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_phone_del(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {params}")
    find_contact = stor_contacts["Contacts"]["data"].find_by_id(params)
    res = find_contact.del_phone(params)
    storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_col([res])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return "contact edit OK"


def contact_del(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


def contact_find(*args, **kwargs):
    params, *_ = args
    search_string = params["string"]
    print(f"contact_add args: {params}")
    find_contact = stor_contacts["Contacts"]["data"].find(search_string)
    # res = find_contact.edit_phone(params)
    # storage_save_file(stor_contacts["Contacts"])
    stor_contacts["Contacts"]["data"].show_col([find_contact])
    # stor_contacts["Contacts"]["data"].show_all([find_contact])

    return find_contact
    return "contact edit OK"


def contact_birthday(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")
    # res = my_storage["Contacts"].birthday_find(params)
    # print(f"result search birthday:\n {res}")
    # return res


def contact_showall(*args, **kwargs):
    params, *_ = args
    for_out = stor_contacts["Contacts"]["data"].data
    # res = stor_contacts["Contacts"]["data"].show_all(for_out)
    res = stor_contacts["Contacts"]["data"].get_all()
    # print (res)
    stor_contacts["Contacts"]["data"].show_col(res)
    # storage_save_file(stor_contacts["Contacts"])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return res


def contact_show(*args, **kwargs):
    params, *_ = args
    print(f"note_add args: {args}")
    print(f"note_add args: {params}")
    print(f"note_add kwargs: {kwargs}")

    return "Note edit OK"
