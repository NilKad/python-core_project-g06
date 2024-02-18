import argparse


def createParser():
    parser = argparse.ArgumentParser(
        prog="myhelper", description="You helper application."
    )
    subparser = parser.add_subparsers(help="sub-command help", dest="command")

    contact_parser_group = subparser.add_parser("contact", help="note help")
    note_parser_group = subparser.add_parser("note", help="note help")
    files_sort_parser = subparser.add_parser("filesort", help="sort files help")

    # note_parser.set_defaults(func=note_parser.print_help())

    subparser = note_parser_group.add_subparsers(
        help="sub note command help", dest="command"
    )

    note_add_parser = subparser.add_parser("add", help="note add help")
    # note_add_parser.set_defaults(func=note_add_parser.print_help())
    note_add_parser.set_defaults(func=handler_note)
    note_add_parser.add_argument(
        "-s",
        "--subject",
        # required=True,
        dest="subject",
        type=str,
        # type=note_in_title,
        help="Input %(dest)s for note",
        # default="",
        # default=note_in_title,
    )
    note_add_parser.add_argument(
        "-c",
        "--content",
        # required=True,
        # dest="content",
        # default="",
        type=str,
        help="Input %(dest)s for note",
    )
    note_add_parser.add_argument(
        "-t",
        "--tags",
        # required=True,
        # dest="content",
        # default="",
        type=str,
        help="\033[31mInput %(dest)s for note\033[0m",
    )

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