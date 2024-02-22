# from ast import Raise
from datetime import datetime
from contacts.contact import Contact

from rich.console import Console
from rich.table import Table

# from contact import Record
# from collections import UserDict
# from contact import Contact

# from contact import FirstName, LastName, Email, Phone, Birthday, Address, Record


class Contacts:
    def __init__(self):
        self.data = []
        self.id = 0

    def find_by_id(self, id):
        id = id["id"]
        for el in self.data:
            if el.id == id:
                return el
        raise ValueError(f"{id} not found")

    def add(self, data):
        # id = self.id
        contact = Contact(data, self.id)
        self.data.append(contact)
        self.id += 1
        return contact

    def set(self, data):
        # id = self.id
        # contact = Contact(data, self.id)
        id = data["id"]
        for_edit = self.find_by_id({"id": id})
        res = for_edit.update_all(data)
        # self.data.append(contact)
        # self.id += 1
        return res

    def delete(self, id):
        for idx in range(len(self.data) + 1):
            if self.data[idx].id == id:
                self.data.pop(idx)
                break

    def find(self, value):
        res = []
        for el in self.data:
            value = value.lower()
            if (
                value in el.first_name.value.lower()
                or value in el.last_name.value.lower()
                or value in el.address.value.lower()
                or value in el.email.value.lower()
                or el.is_contains_phone(value)
            ):
                res.append(el)
        return res

    def get_all(self):
        return self.data

    def show_col(self, data):
        contact_table = Table(title="contacts", show_lines=True, width=125)
        contact_table.add_column("ID", style="white")
        contact_table.add_column("First Name", style="green")
        contact_table.add_column("Last Name", style="green")
        contact_table.add_column("Phones", style="magenta")
        contact_table.add_column("Address", style="yellow")
        contact_table.add_column("Email", style="cyan")
        contact_table.add_column("Birthday", style="white")

        for contact in data:
            # all_phones = ""
            # all_phones = str(data["phones"])
            # for phone in contact["phones"]:
            #     all_phones = all_phones + ", " + phone
            #     all_phones = all_phones.removeprefix(", ")
            all_phones = ""
            for phone in contact.phones:
                all_phones += f", {str(phone)}"
                all_phones = all_phones.removeprefix(", ")

            contact_table.add_row(
                str(contact.id),
                str(contact.first_name),
                str(contact.last_name),
                str(all_phones),
                str(contact.address),
                str(contact.email),
                str(contact.birthday),
            )

        console = Console()
        console.print(contact_table)

    def show_all(self, data):
        for el in data:
            print(el)

    def birthday(self, dates):

        dates_list = dates.split()
        upcoming_birthdays_list = []
        str_start = None
        str_end = None

        if 2 > len(dates_list) >= 1:
            str_start = dates_list[0]
        elif len(dates_list) == 2:
            str_start = dates_list[0]
            str_end = dates_list[1]

        if not str_start:
            date_start = datetime.now().date()
        else:
            date_start = datetime.strptime(str_start, "%Y-%m-%d").date()

        if str_end:
            date_end = datetime.strptime(str_end, "%Y-%m-%d").date()
            for el in self.data:
                date_el = datetime.strptime(el.birthday, "%Y-%m-%d").date()
                if date_el >= date_start and date_el <= date_end:
                    upcoming_birthdays_list.append(el)
        else:
            for el in self.data:
                date_el = datetime.strptime(el.birthday, "%Y-%m-%d").date()
                if date_el == date_start:
                    upcoming_birthdays_list.append(el)

        return upcoming_birthdays_list
