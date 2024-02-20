from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
# Any file where we will have storage of data

# Assuming we have functions like these in your contacts.py
def search_contacts():
    print("Function: search_contacts")

def edit_contact():
    print("Function: edit_contact")

def delete_contact():
    print("Function: delete_contact")

def save_note():
    print("Function: save_note")

def search_notes():
    print("Function: search_notes")

def edit_note():
    print("Function: edit_note")

def delete_note():
    print("Function: delete_note")

def sort_notes():
    print("Function: sort_notes")

def get_contact_list():
    # Example: Get the list of contact names
    return ["John Doe", "Jane Smith", "Alice Johnson"]

def get_contact_ids():
    # Example: Get the list of contact IDs
    return ["1", "2", "3"]

# Map commands to corresponding functions
command_functions = {
    "search_contacts": search_contacts,
    "edit_contact": edit_contact,
    "delete_contact": delete_contact,
    "save_note": save_note,
    "search_notes": search_notes,
    "edit_note": edit_note,
    "delete_note": delete_note,
    "sort_notes": sort_notes
}

contact_names = get_contact_list()
contact_ids = get_contact_ids()

suggestions = list(command_functions.keys()) + contact_names + contact_ids
completer = WordCompleter(suggestions)

def get_suggestions():
    while True:
        user_input = prompt('Enter command: ', completer=completer, auto_suggest=AutoSuggestFromHistory())

        if user_input.lower() == 'exit':
            break

        if user_input in command_functions:
            command_functions[user_input]()
        elif user_input in contact_names:
            print(f"Function: contact_details('{user_input}')")
        elif user_input in contact_ids:
            print(f"Function: contact_details_by_id('{user_input}')")

if __name__ == "__main__":
    get_suggestions()