import argparse
from operator import concat
import shutil
import sys

from my_lib.textc import textc

# from ..lib.textc import textc


#!!!!!!!!!!!!!!!
# size_console = shutil.get_terminal_size()
# print(size_console)
#!!!!!!!!!!!!!!!

print(textc(f"sadadasd", "RED"))


def addition_input(args, req_params, var_in_set=[]):
    args_dict = vars(args)
    new_args_dict = {}
    excl_params = ["command", "func"]

    # print(f"addition_input args: {args}")

    print(textc(f"Press CTRL-C to skeep", "DARKGREY"))
    for key, value in args_dict.items():
        if value in excl_params:
            continue
        if not value:
            while True:
                cur_var = [] if key in new_args_dict else ""
                try:
                    cur_var = input(textc(f"Input {key} [] #: ", "GREEN"))

                    if key in req_params and cur_var == "":
                        print(textc(f"{key} is requared value! please enter", "RED"))
                        continue

                    if key in var_in_set:
                        new_args_dict[key] = set(cur_var.split())
                    else:
                        new_args_dict[key] = cur_var

                    break
                except KeyboardInterrupt as e:
                    # print(f"cur_var: {cur_var} len: {len(cur_var)}")
                    print(textc(f"\nKeyboard pressed Ctrl-C\nKeep input", "YELLOW"))
                    new_args_dict[key] = ""
                    break
        elif key not in excl_params:
            new_args_dict[key] = set(value) if key in var_in_set else value
        # else:
        # new_args_dict[key] = value

    # print(f"new_args: {new_args_dict}")
    return new_args_dict


def handler_exit(args):
    print("!!! exit")
    print(args)
    sys.exit()


def handler_add_note(args):
    # print(f"__handler_add_note args: {args}")
    req_params = ["subject", "content"]
    # excl_params = ["command", "func"]
    variables_in_set = ["tags"]

    res = addition_input(args, req_params, variables_in_set)
    # print(f"____handler_add_note result: {result}")

    return res


def handler_edit_note(args):
    print(f"handler_del_note args: {args}")
    req_params = ["id"]
    excl_params = ["command", "func"]
    excl_params2 = ["command", "func", "id"]
    variables_in_set = ["tags"]

    is_skeep_addition = False
    res = vars(args)
    # проверка на наличие хотя бы одного введенного аргумента,
    # если есть, то не запускать на ввод их интерактивно
    for key, value in res.items():
        if key not in excl_params2 and (
            (isinstance(value, set) and len(value) > 0) or value
        ):
            is_skeep_addition = True
            break
    if not is_skeep_addition:
        res = addition_input(args, req_params, variables_in_set)

    # new_res = list(filter(lambda key, values: values != "", vars(res)))
    # удаление пустых аргументов
    new_res = {}
    for key, value in res.items():
        # print(new_res, type(new_res))
        if (
            key in excl_params
            or (value == "" or not value)
            or (isinstance(value, set) and len(value) == 0)
        ):
            continue
        new_res[key] = value
    return new_res


def handler_del_note(args):
    print(f"handler_del_note args: {args}")
    req_params = ["id"]
    res = addition_input(args, req_params)
    return res


def handler_find_note(args):
    print(f"handler_find_note args: {args}")
    req_params = ["tags"]
    variables_in_set = ["tags"]
    res = addition_input(args, req_params, variables_in_set)
    return res


def handler_findsubject_note(args):
    print(f"handler_findsubject_note args: {args}")
    req_params = ["subject"]
    variables_in_set = ["subject"]
    res = addition_input(args, req_params, variables_in_set)
    return res


def handler_sort_by_tag_note(args):
    print(f"handler_sort_by_tag args: {args}")
    res = addition_input(args, [])

    return res


def handler_show_note(args):
    print(f"handler_find_note args: {args}")
    res = addition_input(args, [])

    return res


def handler_add_contact(args):
    print(f"handler_add_contact args: {args}")
    req_params = ["content"]
    # excl_params = ["command", "func"]
    variables_in_set = ["tags"]

    res = addition_input(args, req_params, variables_in_set)
    # print(f"____handler_add_note result: {result}")

    return res


def handler_edit_contact(args):
    print(f"handler_del_note args: {args}")
    req_params = ["id"]
    excl_params = ["command", "func"]
    excl_params2 = ["command", "func", "id"]
    variables_in_set = ["phone"]

    is_skeep_addition = False
    res = vars(args)
    # проверка на наличие хотя бы одного введенного аргумента,
    # если есть, то не запускать на ввод их интерактивно
    for key, value in res.items():
        if key not in excl_params2 and (
            (isinstance(value, set) and len(value) > 0) or value
        ):
            is_skeep_addition = True
            break
    if not is_skeep_addition:
        res = addition_input(args, req_params, variables_in_set)

    # new_res = list(filter(lambda key, values: values != "", vars(res)))
    # удаление пустых аргументов
    new_res = {}
    for key, value in res.items():
        # print(new_res, type(new_res))
        if (
            key in excl_params
            or (value == "" or not value)
            or (isinstance(value, set) and len(value) == 0)
        ):
            continue
        new_res[key] = value
    return new_res


def handler_del_contact(args):
    print(f"handler_del_contact args: {args}")


def handler_find_by_id_contact(args):
    print(f"handler_find_by_id_contact args: {args}")


def handler_find_contact(args):
    print(f"handler_find_contact args: {args}")


# def handler_birthday_contact(args):
#     print(f"handler_birthday_contact args: {args}")


# def handler_set_firstname_contact(args):
#     print(f"handler_set_firstname_contact args: {args}")


# def handler_set_lastname_contact(args):
#     print(f"handler_set_lastname_contact args: {args}")


# def handler_set_birthday_contact(args):
#     print(f"handler_birthday_firstname_contact args: {args}")


# def handler_set_address_contact(args):
#     print(f"handler_set_address_contact args: {args}")


# def handler_set_email_contact(args):
#     print(f"handler_set_email_contact args: {args}")


def handler_phone_add_contact(args):
    print(f"handler_add_phone_contact args: {args}")


def handler_phone_edit_contact(args):
    print(f"handler_edit_phone_contact args: {args}")


def handler_phone_del_contact(args):
    print(f"handler_del_phone_contact args: {args}")


def handler_birthday_contact(args):
    print(f"handler_birthday_contact args: {args}")


def handler_sort_files(args):
    print(f"handler_sort_files args: {args}")


def create_parser():
    parser = argparse.ArgumentParser(
        prog="myhelper", description="You helper application.", exit_on_error=False
    )

    # parser_main = parser.add_parser()
    # parser.add_argument("exit", dest="exitfsdfsfsdf", help="Exit from programm")
    # parser.add_argument("exit", help="Exit from programm")
    # parser.set_defaults(func=handler_main)

    subparser = parser.add_subparsers(help="sub-command help", dest="command")
    contact_parser_group = subparser.add_parser("contact", help="note help")
    note_parser_group = subparser.add_parser("note", help="note help")
    files_sort_parser = subparser.add_parser("filesort", help="sort files help")
    exit_parser = subparser.add_parser("exit", help="Exit from programm")

    subparser = note_parser_group.add_subparsers(
        help="sub note command help", dest="command"
    )

    note_add_parser = subparser.add_parser("add", help="note add help")
    note_add_parser.set_defaults(func=handler_add_note)
    note_add_parser.add_argument(
        "-s",
        "--subject",
        dest="subject",
        type=str,
        # type=note_in_title,
        help=textc("Input %(dest)s for note", "RED"),
    )
    note_add_parser.add_argument(
        "-c",
        "--content",
        # required=True,
        dest="content",
        # default="",
        type=str,
        help=textc("Input %(dest)s for note", "RED"),
    )
    note_add_parser.add_argument(
        "-t",
        "--tags",
        dest="tags",
        type=str,
        help="\033[31mInput %(dest)s for note\033[0m",
        nargs="+",
    )

    note_edit_parser = subparser.add_parser("edit", help="Edit Note")
    note_edit_parser.set_defaults(func=handler_edit_note)
    note_edit_parser.add_argument("id", type=int)
    note_edit_parser.add_argument(
        "-s",
        "--subject",
        dest="subject",
        type=str,
        help=textc("Input %(dest)s for note", "RED"),
    )
    note_edit_parser.add_argument(
        "-c",
        "--content",
        dest="content",
        type=str,
        help=textc("Input %(dest)s for note", "RED"),
    )
    note_edit_parser.add_argument(
        "-t",
        "--tags",
        dest="tags",
        type=str,
        help="\033[31mInput %(dest)s for note\033[0m",
        nargs="+",
    )

    note_del_parser = subparser.add_parser("del", help="Delete note by id")
    note_del_parser.set_defaults(func=handler_del_note)
    note_del_parser.add_argument(dest="id", type=int)

    note_find_parser = subparser.add_parser("find", help="Find note by tag")
    note_find_parser.set_defaults(func=handler_find_note)
    note_find_parser.add_argument(dest="tags", nargs="*", help="Tags for search")

    note_findsubject_parser = subparser.add_parser(
        "findsubject", help="Find note by subject"
    )
    note_findsubject_parser.set_defaults(func=handler_findsubject_note)
    note_findsubject_parser.add_argument(
        dest="subject", nargs="*", help="Subject for search"
    )

    note_sort_by_tag_parser = subparser.add_parser(
        "sorttag", help="note sort by tag in record"
    )
    note_sort_by_tag_parser.set_defaults(func=handler_sort_by_tag_note)

    note_show_parser = subparser.add_parser("show", help="Show All notes")
    note_show_parser.set_defaults(func=handler_show_note)
    # note_show_parser.add_argument(dest="tag", nargs="*", help="Search Note by tag")

    subparser = contact_parser_group.add_subparsers(
        help="sub contact command help", dest="command"
    )
    contact_add_parser = subparser.add_parser("add", help="Contact add help")
    contact_add_parser.set_defaults(func=handler_add_contact)
    contact_add_parser.add_argument(
        "-f",
        "--firstname",
        dest="first_name",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_add_parser.add_argument(
        "-l",
        "--lastname",
        dest="last_name",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_add_parser.add_argument(
        "-p",
        "--phone",
        dest="phones",
        type=str,
        nargs="+",
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_add_parser.add_argument(
        "-a",
        "--address",
        dest="address",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_add_parser.add_argument(
        "-b",
        "--birthday",
        dest="birthday",
        type=str,
        help=textc("Input %(dest)s for contact in format 2022-02-02", "RED"),
    )

    contact_edit_parser = subparser.add_parser("set", help="contact add help")

    contact_edit_parser.set_defaults(func=handler_edit_contact)
    contact_edit_parser.add_argument("id", type=int, help="contact ID")
    contact_edit_parser.add_argument(
        "-f",
        "--firstname",
        dest="first_name",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_edit_parser.add_argument(
        "-l",
        "--lastname",
        dest="last_name",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_edit_parser.add_argument(
        "-p",
        "--phone",
        dest="phones",
        type=str,
        nargs="+",
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_edit_parser.add_argument(
        "-a",
        "--address",
        dest="address",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_edit_parser.add_argument(
        "-b",
        "--birthday",
        dest="birthday",
        type=str,
        help=textc("Input %(dest)s for contact in format 2022-02-02", "RED"),
    )

    contact_phone_group = subparser.add_parser("phone", help="contact phone help")
    subparser_phone = contact_phone_group.add_subparsers(
        help="sub phone in contact command help", dest="command"
    )

    contact_phone_add_parser = subparser_phone.add_parser(
        "add", help="Add phone(s) to Contact"
    )
    contact_phone_add_parser.set_defaults(func=handler_phone_add_contact)
    contact_phone_add_parser.add_argument("id", type=int, help="contact ID")
    contact_phone_add_parser.add_argument(
        "-p",
        "--phone",
        dest="phones",
        type=str,
        nargs="+",
        help=textc("Input %(dest)s for contact", "RED"),
    )

    contact_phone_edit_parser = subparser.add_parser(
        "edit", help="Edit phone(s) to Contact"
    )
    contact_phone_edit_parser.set_defaults(func=handler_phone_add_contact)
    contact_phone_edit_parser.add_argument("-id", type=int, help="contact ID")
    contact_phone_edit_parser.add_argument(
        "-p",
        # nargs=2,
        dest="phones",
        type=str,
        help=textc("Input old_phone and new_phone for contact by id", "RED"),
    )

    contact_phone_del_parser = subparser.add_parser(
        "del", help="Delete phone to Contact"
    )
    contact_phone_del_parser.set_defaults(func=handler_phone_add_contact)
    contact_phone_del_parser.add_argument("-id", type=int, help="contact ID")
    contact_phone_del_parser.add_argument(
        "-p",
        # nargs=2,
        # dest="phones",
        type=str,
        help=textc("Input %(dest)s for delete in contact", "RED"),
    )

    contact_find_parser = subparser.add_parser("find", help="Contact find")
    contact_find_parser.set_defaults(func=handler_find_contact)
    contact_find_parser.add_argument(
        "string", type=str, help="Input %(dest)s for search in contacts"
    )

    contact_find_by_id_parser = subparser.add_parser(
        "findbyid", help="Contact find by id"
    )
    contact_find_by_id_parser.set_defaults(func=handler_find_by_id_contact)
    contact_find_by_id_parser.add_argument("id", type=int, help="contact ID")

    contact_birthday_parser = subparser.add_parser(
        "birthday", help="Find birthday in Contacts"
    )
    contact_birthday_parser.set_defaults(func=handler_birthday_contact)
    contact_birthday_parser.add_argument(
        "date",
        type=str,
        nargs="+",
        help="Input %(dest)s birthday for search in contacts",
    )

    files_sort_parser.set_defaults(func=handler_sort_files)
    files_sort_parser.add_argument(
        "-s", type=str, help="Source path with files for sorting"
    )
    files_sort_parser.add_argument(
        "-d", type=str, help="Destination path for save files"
    )

    exit_parser.set_defaults(func=handler_exit)

    # parser.add_argument("-n", "--name", nargs="?", help="This is the 'a' variable")
    # parser.add_argument("note", help="This is the note ")

    # parent_parser = argparse.ArgumentParser(add_help=False)
    # parent_parser.add_argument("--parrent", type=int)

    # note_parser = argparse.ArgumentParser(parents=[parent_parser])
    # note_parser.add_argument("note")
    # return parser
    # return parser.parse_args()
    return parser


if __name__ == "__main__":
    # print(sys.argv)

    # parser = createParser()
    args = create_parser()
    print(f"args: {args}")
    print(f"args.command: {args.command}")
    # print(not args)
    # print(f"vars(args): {vars(args)}")
    # print(not vars(args))
    # Namespace()

    args.func(args)
    print(f"new args: {args}")

    # if namespace == None:
    #     parser.print_help()
    # # print(namespace.name)

    # print(f"parser: {parser}")
    # print(f"parser2: {parser.print_usage}")
    # print(f"parser3: {dir(parser)}")
    # print(f"\nparser4: {parser._registries.parsers}")
