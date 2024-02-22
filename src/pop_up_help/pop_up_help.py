from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from parser_act.parser_act import (
    handler_add_contact,
    handler_add_note,
    handler_birthday_contact,
    handler_del_contact,
    handler_del_note,
    handler_find_by_id_contact,
    handler_find_contact,
    handler_find_note,
    handler_findsubject_note,
    handler_phone_add_contact,
    handler_phone_del_contact,
    handler_phone_edit_contact,
    handler_set_contact,
    handler_set_note,
    handler_show_contact,
    handler_show_note,
    handler_sort_by_tag_note,
    handler_sort_files,
)


top_level_commands = {
    "contact": {
        "add": handler_add_contact,
        "edit": handler_set_contact,
        "delete": handler_del_contact,
        "find": handler_find_contact,
        "findbyid": handler_find_by_id_contact,
        "phone": {
            "add": handler_phone_add_contact,
            "edit": handler_phone_edit_contact,
            "delete": handler_phone_del_contact,
        },
        "birthday": handler_birthday_contact,
        "show": handler_show_contact,
    },
    "phone": {
        "add": handler_phone_add_contact,
        "delete": handler_phone_del_contact,
    },
    "notes": {
        "add": handler_add_note,
        "edit": handler_set_note,
        "delete": handler_del_note,
        "find": handler_find_note,
        "findsubject": handler_findsubject_note,
        "sorttag": handler_sort_by_tag_note,
        "show": handler_show_note,
    },
    "filesort": {
        "sort": handler_sort_files,
    },
}

all_commands = []
for top_command, sub_commands in top_level_commands.items():
    all_commands.append(top_command)
    if isinstance(sub_commands, dict):
        all_commands.extend(
            [f"{top_command} {sub_command}" for sub_command in sub_commands]
        )

completer = WordCompleter(all_commands)


def get_suggestions():
    while True:
        user_input = prompt(
            "Enter command: ",
            completer=completer,
            auto_suggest=AutoSuggestFromHistory(),
        )

        if user_input.lower() == "exit":
            break

        parts = user_input.split()
        current_level = top_level_commands

        for part in parts:
            if part in current_level:
                current_level = current_level[part]
            else:
                print(f"Unknown command: {user_input}")
                break
        else:
            if callable(current_level):
                current_level()
            else:
                print(f"Unknown command: {user_input}")


if __name__ == "__main__":
    get_suggestions()
