import argparse
from operator import concat
import shutil
import sys

from lib.textc import textc

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


def handler_del_contact(args):
    print(f"handler_del_contact args: {args}")


def handler_find_by_id_contact(args):
    print(f"handler_find_by_id_contact args: {args}")


def handler_find_contact(args):
    print(f"handler_find_contact args: {args}")


def handler_birthday_contact(args):
    print(f"handler_birthday_contact args: {args}")


def handler_set_firstname_contact(args):
    print(f"handler_set_firstname_contact args: {args}")


def handler_set_lastname_contact(args):
    print(f"handler_set_lastname_contact args: {args}")


def handler_set_birthday_contact(args):
    print(f"handler_birthday_firstname_contact args: {args}")


def handler_set_address_contact(args):
    print(f"handler_set_address_contact args: {args}")


def handler_set_email_contact(args):
    print(f"handler_set_email_contact args: {args}")


def handler_add_phone_contact(args):
    print(f"handler_add_phone_contact args: {args}")


def handler_edit_phone_contact(args):
    print(f"handler_edit_phone_contact args: {args}")


def handler_del_phone_contact(args):
    print(f"handler_del_phone_contact args: {args}")


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

    # note_parser.set_defaults(func=note_parser.print_help())

    subparser = note_parser_group.add_subparsers(
        help="sub note command help", dest="command"
    )

    note_add_parser = subparser.add_parser("add", help="note add help")
    # note_add_parser.set_defaults(func=note_add_parser.print_help())
    note_add_parser.set_defaults(func=handler_add_note)
    note_add_parser.add_argument(
        "-s",
        "--subject",
        # required=True,
        dest="subject",
        type=str,
        # type=note_in_title,
        help=textc("Input %(dest)s for note", "RED"),
        # default="",
        # default=note_in_title,
        # metavar="ADD--AAA",
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
        # required=True,
        dest="tags",
        # default="",
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
    contact_add_parser = subparser.add_parser("add", help="contact add help")
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
        nargs='+',
        help=textc("Input %(dest)s for contact", "RED"),
    )
    contact_add_parser.add_argument(
        "-a",
        "--address",
        dest="address",
        type=str,
        help=textc("Input %(dest)s for contact", "RED"),
    )
    

    exit_parser.set_defaults(func=handler_exit)

    # exit_parser.add_argument(help)

    # print("-----------------")
    # print(parser.format_help())
    # print(textc("dsdadsad", "RED"))
    # print("\033[38;5;245m@@@@@@@@@@@@@@@@@\033[0m")
    # print("\033[250m1234\033[0m")

    # note_add_parser = note_parser.add_subparsers(help="L3 subparser", dest="command")
    # note_add_parser.add_parser("add", help="note add help")
    # note_add_parser.set_defaults(func=handler_note)
    # note_add_parser.add_argument("test")

    # note_add_parser =
    # contact_parser = subparser.add_parser("contact", help="contact help")
    # contact_parser.add_argument(
    #     "-fn",
    #     "--FirstName",
    #     default="",
    #     dest="first_name",
    #     type=str,
    #     help="Input First name",
    # )
    # contact_parser.add_argument(
    #     "-ln",
    #     "--LastName",
    #     default="",
    #     dest="last_name",
    #     type=str,
    #     help="Input Last name",
    # )

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
