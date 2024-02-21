from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from ctrl_contacts import (
    contact_add,
    contact_find_by_id,
    contact_set,
    contact_phone_add,
    contact_phone_edit,
    contact_phone_del,
    contact_del,
    contact_find,
    contact_birthday,
    contact_showall,
    contact_show,
)

from ctrl_notes import (
    note_add,
    note_set,
    note_del,
    note_find,
    note_findsubject,
    note_sort_by_tag,
    note_show,
)

top_level_commands = {
    "contact": {
        "add": contact_add,
        "find_by_id": contact_find_by_id,
        "set": contact_set,
        "phone": {
            "add": contact_phone_add,
            "edit": contact_phone_edit,
            "del": contact_phone_del,
        },
        "del": contact_del,
        "find": contact_find,
        "birthday": contact_birthday,
        "showall": contact_showall,
        "show": contact_show,
    },
    "notes": {
        "add": note_add,
        "set": note_set,
        "del": note_del,
        "find": note_find,
        "findsubject": note_findsubject,
        "sort_by_tag": note_sort_by_tag,
        "show": note_show,
    }
}

all_commands = []
for top_command, sub_commands in top_level_commands.items():
    all_commands.append(top_command)
    if isinstance(sub_commands, dict):
        all_commands.extend([f"{top_command} {sub_command}" for sub_command in sub_commands])

completer = WordCompleter(all_commands)

def get_suggestions():
    while True:
        user_input = prompt('Enter command: ', completer=completer,
                            auto_suggest=AutoSuggestFromHistory())

        if user_input.lower() == 'exit':
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