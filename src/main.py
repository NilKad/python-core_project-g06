import os
import sys
from contacts.contacts import Contacts
from my_lib.textc import textc
from notes.notes import Notes

from parser_act.parser_act import my_parser

from save_load.save_load import storage_load_file, storage_save_file

# global my_storage
global my_storage
my_storage = {}
my_storage_list = {Notes: "storage_notes.bin", Contacts: "storage_contacts.bin"}


# print(my_storage)


def get_storage_contacts():
    return my_storage_list
    pass


def storage_init(stor_class, stor_path):
    class_name = stor_class.__name__
    my_storage[class_name] = {}
    my_storage[class_name]["data"] = stor_class()
    my_storage[class_name]["path"] = stor_path


def storage_load():
    for stor_class, stor_path in my_storage_list.items():

        if os.path.exists(stor_path):
            storage_init(stor_class, stor_path)
            try:
                storage_load_file(my_storage[stor_class.__name__])
            except Exception:
                print("!!!Error load. Save New structore")
                storage_save_file(my_storage[stor_class.__name__])
                print(type(Exception))
        else:
            storage_init(stor_class, stor_path)
            storage_save_file(my_storage[stor_class.__name__])


def main():
    storage_load()
    parser_main = my_parser()
    # args.parse_args(["note", "-h"])

    # create_parser()
    while True:
        command_input = input("Input command: ")

        if command_input == "":
            continue
        command_split = command_input.split()
        try:

            parser_res = parser_main.parse_args(command_split)
            print(textc(f"----- main args: {parser_res}", "GREEN"))
            result_dict = parser_res.func(parser_res)
            print(textc(f"result_dict: {result_dict}", "YELLOW"))
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
