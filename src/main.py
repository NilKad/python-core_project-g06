import argparse
import sys
from parser_act import create_parser

# phonebook
# contact
# addressbook

# note-add -n ""
# note-del id
# note-add
# note-add
# note-add


# sort-files

# todo


# import contacts

# from contact import Contacts


# print(dir(contacts))

# from contacts import Contacts
# from contacts import Contacts
# from contacts import *
# import contacts


def main():
    # pass
    args = create_parser()
    # args.parse_args(["note", "-h"])

    # create_parser()
    while True:
        command_input = input("Input command: ")

        if command_input == "":
            continue

        try:
            args = args.parse_args(command_input.split())
            print(args)
            args.func(args)
        except KeyboardInterrupt:
            print("--------KeyboardInterrupt--------Exception, e:")
            sys.exit()
        except Exception as e:
            print("----------------Exception, e:", type(e))
        except SystemExit as se:
            print("--------Systemexit--------Exception", se)

        except:
            print("--------ALL--------Exception")


# parser_my = create_parser()

main()
