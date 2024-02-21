from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

def search_contacts():
    print("Function: search_contacts")


def edit_contact():
    print("Function: edit_contact")


def delete_contact():
    print("Function: delete_contact")


def add_phone():
    print("Function: add_phone")


def edit_phone():
    print("Function: edit_phone")


def delete_phone():
    print("Function: delete_phone")


def add_note():
    print("Function: add_note")


def edit_note():
    print("Function: edit_note")


def delete_note():
    print("Function: delete_note")


# Словари функций для каждого уровня меню
top_level_commands = {
    "contact": {
        "add": add_contact,
        "edit": edit_contact,
        "delete": delete_contact,
    },
    "phone": {
        "add": add_phone,
        "edit": edit_phone,
        "delete": delete_phone,
    },
    "notes": {
        "add": add_note,
        "edit": edit_note,
        "delete": delete_note,
    }
}

# Создаем список всех команд для автодополнения
all_commands = []
for top_command, sub_commands in top_level_commands.items():
    all_commands.append(top_command)
    all_commands.extend(
        [f"{top_command} {sub_command}" for sub_command in sub_commands])

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