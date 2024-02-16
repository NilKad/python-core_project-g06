from .contact import *

print("init Contacts")

conf = {
    "name": "contact",
    "actions": [
        {"contact-add": {"def": "def", "args": ["Contact"], "help": "this help text"}},
        {
            "phone-add": {
                "def": "def",
                "args": ["id_contact", "phone"],
                "help": "this help for phone-add",
            }
        },
    ],
}

# __all__ = ["Contacts"]
# __name__ = Contacts
