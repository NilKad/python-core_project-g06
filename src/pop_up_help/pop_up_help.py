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


    # Словари функций для каждого элемента
contact_commands = {
    "search_contacts": search_contacts,
    "edit_contact": edit_contact,
    "delete_contact": delete_contact,
}

phone_commands = {
    "add_phone": add_phone,
    "edit_phone": edit_phone,
    "delete_phone": delete_phone,
}
notes_commands = {
    "add_note": add_note,
    "edit_note": edit_note,
    "delete_note": delete_note,

}
all_commands = list(contact_commands.keys()) + list(phone_commands.keys())
completer = WordCompleter(all_commands)

def get_suggestions():
    while True:
        user_input = prompt('Enter command: ', completer=completer,
                            auto_suggest=AutoSuggestFromHistory())

        if user_input.lower() == 'exit':
            break

        if user_input in contact_commands:
            contact_commands[user_input]()
        elif user_input in phone_commands:
            phone_commands[user_input]()

if __name__ == "__main__":
    get_suggestions()
