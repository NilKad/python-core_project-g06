# import startup
import sys
from stor_svc import storage_load
from my_lib.textc import textc
from parser_act.parser_act import my_parser

# from save_load.save_load import storage_load_file, storage_save_file


def main():
    storage_load()
    parser_main = my_parser()

    while True:
        command_input = input("Input command: ")

        if command_input == "":
            continue
        command_split = command_input.split()
        try:

            parser_res = parser_main.parse_args(command_split)
            print(textc(f"----- main args: {parser_res}", "GREEN"))
            # result_dict = parser_res.func(parser_res)
            parser_res.func(parser_res)
            # print(textc(f"result_dict: {result_dict}", "YELLOW"))
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
