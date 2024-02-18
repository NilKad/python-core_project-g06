import argparse
import shutil
import sys

from lib.textc import textc

# from ..lib.textc import textc


#!!!!!!!!!!!!!!!
# size_console = shutil.get_terminal_size()
# print(size_console)
#!!!!!!!!!!!!!!!

print(textc(f"sadadasd", "RED"))


def addition_input(args, req_params, var_in_set):
    args_dict = vars(args)
    new_args_dict = {}
    excl_params = ["command", "func"]

    print(f"addition_input args: {args}")

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
                    print(f"cur_var: {cur_var} len: {len(cur_var)}")
                    print(textc(f"\nKeyboard pressed Ctrl-C\nKeep input", "YELLOW"))
                    new_args_dict[key] = ""
                    break
        elif key not in excl_params:
            new_args_dict[key] = ""

    print(f"new_args: {new_args_dict}")
    return new_args_dict


def handler_exit(args):
    print("!!! exit")
    print(args)
    sys.exit()


def handler_add_note(args):
    print(f"args: {args}")
    req_params = ["subject", "content"]
    # excl_params = ["command", "func"]
    variables_in_set = ["tags"]

    result = addition_input(args, req_params, variables_in_set)
    print(f"result: {result}")

    return result


def createParser():
    parser = argparse.ArgumentParser(
        prog="myhelper", description="You helper application."
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
        # dest="content",
        # default="",
        type=str,
        help=textc("Input %(dest)s for note", "RED"),
    )
    note_add_parser.add_argument(
        "-t",
        "--tags",
        # required=True,
        # dest="content",
        # default="",
        type=str,
        help="\033[31mInput %(dest)s for note\033[0m",
        nargs="+",
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
    return parser.parse_args()


if __name__ == "__main__":
    # print(sys.argv)

    # parser = createParser()
    args = createParser()
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
