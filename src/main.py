# phonebook
# contact
# addressbook

# notes

# sort-files

# todo


# import contacts

from datetime import datetime, timedelta

# from contact import Contacts


# print(dir(contacts))

# from contacts import Contacts
# from contacts import Contacts
# from contacts import *
# import contacts


# m = Contacts()
# print(m.record)

# print(m.__)
# print(m.constacts)
# print(m.constacts)
# my_record = m.record
# print(my_record)

cur_date = datetime.now()
# cur_date = datetime.strptime("2023-12-28", "%Y-%m-%d")

br = datetime.now() + timedelta(days=6)
br_minus = datetime.now() - timedelta(days=6)
upcoming_date = datetime.now() + timedelta(days=10)
print(f"\ncur_date: {cur_date}\nbr: {br}\nupcoming_date: {upcoming_date}\n")

# if cur_date <= br < upcoming_date:
if cur_date <= br < upcoming_date:
    print("True")
else:
    print("False")

if cur_date <= br_minus < upcoming_date:
    print("True")
else:
    print("False")


def handler_hello():
    pass


# if birthday_date and current_date <= birthday_date < upcoming_date:


command_list = {
    "hello": handler_hello,
    # "add": handler_add,  # add new contact: Name Phone
    # "del": handler_del,  # del contact: Name
    # "add phone": handler_add_phone,  # added phone to contact: Name phone
    # "edit phone": handler_edit_phone,  # change phone: Name OldPhone NewPhone
    # "remove phone": handler_remove_phone,  # del phone in contact: Name phone
    # "birthday": handler_set_birthday,  # set birthday to contact: Name date_birthday
    # "show all": handler_show_all,
    # "find": handler_find,  # find name or phone: Name|Phone
    # "save": handler_save,  # save Addressbook
    # "load": handler_load,  # load Addressbook
    # "good bye": handler_end_program,
    # "close": handler_end_program,
    # "exit": handler_end_program,
    # "quit": handler_end_program,
}


def command_parse(string):
    string_lower = string.lower().strip()
    f_list = string_lower.split()
    f_list1 = f_list[0]
    f_list2 = " ".join(f_list[0:2])

    command_find = list(
        filter(
            lambda key: string_lower.startswith(key)
            and (f_list1 == key or f_list2 == key),
            command_list.keys(),
        )
    )

    if len(command_find) == 0:
        print("command not found")
        return

    command_current = command_list[command_find[0]]
    command_parameters = string.replace(command_find[0], "").strip().split()
    res = command_current(command_parameters)
    return res


def main():
    while True:
        command_input = input("Input command: ")

        if command_input == "":
            continue
        res = command_parse(command_input)
        print(res)
