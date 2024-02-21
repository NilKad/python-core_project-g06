# from contacts import birthday

# from main import get_storage_contacts

# from main import my_storage

# import __main__

# contacts_storage = my_storage['Contacts']
# contacts_storage_data = contacts_storage['data']
# global my_storage

# print(__main__.my_storage)

# print(get_storage_contacts())
# my_storage_conta


def contact_add(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact add OK"


def contact_set(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")

    return "contact edit OK"


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


def contact_show(*args, **kwargs):
    params, *_ = args
    print(f"note_add args: {args}")
    print(f"note_add args: {params}")
    print(f"note_add kwargs: {kwargs}")

    return "Note edit OK"
