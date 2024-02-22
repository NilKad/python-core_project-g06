from save_load.save_load import storage_save_file
from stor_svc import (
    get_stor_note,
    get_stor_note_box,
    get_stor_note_data,
    get_stor_note_path,
)

stor_notes = get_stor_note()

stor_note_box = get_stor_note_box
stor_note_data = get_stor_note_data
stor_note_path = get_stor_note_path


def note_add(*args, **kwargs):
    params, *_ = args
    res = stor_notes["Notes"]["data"].add(params)
    storage_save_file(stor_notes["Notes"])
    stor_notes["Notes"]["data"].show_all_notes([res])

    # stor_notes["Notes"]["data"].show_all([res])
    # stor_notes["Notes"]["data"].show_by_id(res)

    return res


def note_find_by_id(id):
    res = stor_notes["Notes"]["data"].find_by_id(id)
    stor_notes["Notes"]["data"].show_all_notes([res])

    # stor_notes["Notes"]["data"].show_all_one([res])

    # stor_notes["Notes"]["data"].show_one([res])
    # stor_notes["Notes"]["data"].show_all([res])
    # stor_notes["Notes"]["data"].show_all(res)
    return res


def note_set(args):
    print(f"note_set args: {args}")
    find_note = stor_notes["Notes"]["data"].find_by_id(args["id"])

    res = find_note.update_all(args)
    storage_save_file(stor_notes["Notes"])
    # stor_notes["Notes"]["data"].show_one()
    stor_notes["Notes"]["data"].show_all_notes([res])

    # stor_notes["Notes"]["data"].show_notes(res)
    return res


def note_del(args):
    print(f"note_del args: {args}")
    res = stor_notes["Notes"]["data"].delete(args["id"])
    storage_save_file(stor_notes["Notes"])
    return res


def note_find(*args, **kwargs):
    params, *_ = args
    print(f"note_add args: {params}")
    res = stor_notes["Notes"]["data"].find_by_tags(params)
    # stor_notes["Notes"]["data"].show_all(res)
    stor_notes["Notes"]["data"].show_all_notes([res])

    return res


def note_findsubject(*args, **kwargs):
    params, *_ = args

    print(f"note_add args: {params}")
    # res = stor_notes["Notes"]["data"].find_by_subject(params["subject"])
    res = stor_notes["Notes"]["data"].show_by_subject(params["subject"])

    # stor_notes["Notes"]["data"].show_all(res)
    return res


# show_by_subject


def note_sort_by_tag(*args, **kwargs):
    # params, *_ = args
    # print ('AAAAAAAA')
    # print(f"note_add args: {params}")
    # stor_notes["Notes"]["data"].sort_by_tag()
    stor_notes["Notes"]["data"].sort_by_tag()

    return "Note edit OK"


def note_show(*args, **kwargs):
    params, *_ = args
    print(f"note_add args: {args}")
    print(f"note_add args: {params}")
    print(f"note_add kwargs: {kwargs}")

    return "Note edit OK"


def note_showall(*args, **kwargs):
    params, *_ = args
    for_out = stor_notes["Notes"]["data"].data
    # res = stor_notes["Notes"]["data"].show_all(for_out)
    stor_notes["Notes"]["data"].show_all_notes(for_out)
    # storage_save_file(stor_contacts["Contacts"])
    # stor_contacts["Contacts"]["data"].show_all([res])
    return
