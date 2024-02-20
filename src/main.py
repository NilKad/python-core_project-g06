import os
import pathlib
import sys
from my_lib.textc import textc
from parser_act import create_parser

my_storage = {}
STORAGE_PATH = "data_storage.bin"


# t = os.path(STORAGE_PATH)
print(f"STORAGE_PATH: {STORAGE_PATH}")
# print(f"t: : {t}")


def storage_load():
    if os.path.exists(STORAGE_PATH):
        pass
        try:
            
            pass
        except Exception:
            print(type(Exception))

    try:
        pass
        # STORAGE_PATH.ise
    except:
        print("!!!!!!!!!!!!!!! Exception")

        pass


def main():
    # pass
    storage_load()
    parser_main = create_parser()
    # args.parse_args(["note", "-h"])

    # create_parser()
    while False:
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
