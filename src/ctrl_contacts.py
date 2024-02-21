# from contacts.contacts import birthday_find

import contacts.contacts as ctrl

from main import my_storage
from save_load.save_load import storage_save_file



def contact_add(*args, **kwargs):
    params, *_ = args
    print(f"contact_add args: {args}")
    print(f"contact_add args: {params}")
    print(f"contact_add kwargs: {kwargs}")
    res = ctrl.add(params)

    storage_save_file(my_storage["Contacts"])
    return res


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
    res = my_storage["Contacts"].birthday_find(params)
    print(f"result search birthday:\n {res}")
    return res



def contact_show(*args, **kwargs):
    params, *_ = args
    print(f"note_add args: {args}")
    print(f"note_add args: {params}")
    print(f"note_add kwargs: {kwargs}")

    return "Note edit OK"
