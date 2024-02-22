from collections import UserList
from rich.console import Console
from rich.table import Table

from notes.note import Note
from save_load.save_load import storage_load_file, storage_save_file


class Notes:
    # __id = 0

    def __init__(self):
        self.stor = {}
        self.stor["data"] = []
        self.path = "storage_note.bin"
        self.load()
        # self.__id = 0
        # self.stor.data = []

    def add(self, args):
        args["id"] = self.stor.data["id"]
        note = Note(args)
        # note.id = self.__id
        self.stor.data.append(note)
        self.stor.id += 1
        return note

    def find_by_id(self, id):
        # id = id["id"]
        for el in self.stor.data:
            if el.id == id:
                print("FIND NOTE!!!!!")
                return el
        raise ValueError(f"{id} not found")

    def find_by_tags(self, args):
        result = []
        for note in self.stor.data:
            for el in args["tags"]:
                if el in note.tags:
                    result.append(note)
        return result

    def show_by_tags(self, args):
        result = self.find_by_tags(args)

        contact_table = Table(title="Find by tag", show_lines=True, width=125)
        contact_table.add_column("Tag", style="magenta")
        contact_table.add_column("ID", style="cyan")
        contact_table.add_column("Title", style="yellow")
        contact_table.add_column("Text", style="green")

        for note in result:
            contact_table.add_row(
                args["tags"], str(note.ID), note.subject, note.content
            )
        console = Console()
        console.print(contact_table)

    def sort_by_tag(self):
        result = {}
        for note in self.stor.data:
            for tag in note.tags:
                if tag not in result.keys():
                    result[tag] = [note]
                else:
                    result[tag].append(note)

        contact_table = Table(title="Sort by tag", show_lines=True, width=125)
        contact_table.add_column("Tag", style="magenta")
        contact_table.add_column("ID", style="cyan")
        contact_table.add_column("Title", style="yellow")
        contact_table.add_column("Text", style="green")

        for key, value in result.items():
            for elem in value:
                contact_table.add_row(key, str(elem.id), elem.subject, elem.content)

        console = Console()
        console.print(contact_table)

    def show_by_id(self, id):
        for note in self.stor.data:
            if note.ID == id:
                all_tag = ""
                for tag in note.tag:
                    all_tag = all_tag + ", " + tag
                    all_tag = all_tag.removeprefix(", ")
                contact_table = Table(title="Find by ID", show_lines=True, width=125)
                contact_table.add_column("ID", style="cyan")
                contact_table.add_column("Tag", style="magenta")
                contact_table.add_column("Title", style="yellow")
                contact_table.add_column("Text", style="green")

                contact_table.add_row(str(note.ID), all_tag, note.subject, note.content)

                console = Console()
                console.print(contact_table)

    def find_by_subject(self, subject):
        result = []
        for note in self.stor.data:
            # if str(note.subject).find(subject):
            if note.subject.find(subject) >= 0:
                result.append(note)
            # all_tag = ""
            # for tag in note.tag:
            #     all_tag = all_tag + ", " + tag
            #     all_tag = all_tag.removeprefix(", ")
        return result

    def show_by_subject(self, subject):
        result = []
        for note in self.stor.data:
            if subject == note.subject:
                result.append(note)
            all_tag = ""
            for tag in note.tag:
                all_tag = all_tag + ", " + tag
                all_tag = all_tag.removeprefix(", ")
        contact_table = Table(title="Find by title", show_lines=True, width=125)
        contact_table.add_column("ID", style="cyan")
        contact_table.add_column("Tag", style="magenta")
        contact_table.add_column("Title", style="yellow")
        contact_table.add_column("Text", style="green")

        for note in result:
            contact_table.add_row(str(note.ID), all_tag, note.subject, note.content)

        console = Console()
        console.print(contact_table)

    def delete(self, id):
        for note in self.stor.data:
            if note.id == id:
                self.stor.data.remove(note)
                return
        # self.stor.data.remove(obj)
        return

    def show_all_notes(self):
        contact_table = Table(title="All notes", show_lines=True, width=125)
        contact_table.add_column("ID", style="cyan")
        contact_table.add_column("Tag", style="magenta")
        contact_table.add_column("Title", style="yellow")
        contact_table.add_column("Text", style="green")

        for note in self.stor.data:
            all_tag = ""
            for tag in note.tag:
                all_tag = all_tag + ", " + tag
                all_tag = all_tag.removeprefix(", ")
            contact_table.add_row(str(note.ID), all_tag, note.subject, note.content)

        console = Console()
        console.print(contact_table)

    def show_all(self, data):
        for el in data:
            print(el)

    def save(self):
        storage_save_file(self)

    def load(self):
        storage_load_file(self)
