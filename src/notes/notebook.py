from collections import UserList
from rich.console import Console
from rich.table import Table




class Notebook(UserList):
    __id = 1
    def add_note(self, note):
        note.ID = self.__id
        self.data.append(note)
        self.__id += 1


    def find_by_tag(self, tag):
        result = []
        for note in self.data:
            if tag in note.tag:
                result.append(note)

        contact_table = Table(title='Find by tag', show_lines=True, width=125)
        contact_table.add_column('Tag', style='magenta')
        contact_table.add_column('ID', style='cyan')
        contact_table.add_column('Title', style='yellow')
        contact_table.add_column('Text', style='green')           

        for note in result:
            contact_table.add_row(tag, str(note.ID), note.title, note.text)

        console = Console()
        console.print(contact_table)
    

    def sort_by_tag(self):
        result = {}
        for note in self:
            for tag in note.tag:
                if tag not in result.keys():
                    result[tag] = [note]
                else:
                    result[tag].append(note)

        contact_table = Table(title='Sort by tag', show_lines=True, width=125)
        contact_table.add_column('Tag', style='magenta')
        contact_table.add_column('ID', style='cyan')
        contact_table.add_column('Title', style='yellow')
        contact_table.add_column('Text', style='green')           

        for key, value in result.items():
            for elem in value:
                contact_table.add_row(key, str(elem.ID), elem.title, elem.text)

        console = Console()
        console.print(contact_table)
         

    def find_by_id(self, id):
        for note in self.data:
            if note.ID == id:
                all_tag = ''
                for tag in note.tag:
                    all_tag = all_tag + ', ' + tag
                    all_tag = all_tag.removeprefix(', ')
                contact_table = Table(title='Find by ID', show_lines=True, width=125)
                contact_table.add_column('ID', style='cyan')
                contact_table.add_column('Tag', style='magenta')
                contact_table.add_column('Title', style='yellow')
                contact_table.add_column('Text', style='green')           

                contact_table.add_row(str(note.ID), all_tag, note.title, note.text)

                console = Console()
                console.print(contact_table)
            

    def find_by_title(self, title):
        result = []
        for note in self.data:
            if title == note.title:
                result.append(note)
            all_tag = ''
            for tag in note.tag:
                all_tag = all_tag + ', ' + tag
                all_tag = all_tag.removeprefix(', ')       

        contact_table = Table(title='Find by title', show_lines=True, width=125)
        contact_table.add_column('ID', style='cyan')
        contact_table.add_column('Tag', style='magenta')
        contact_table.add_column('Title', style='yellow')
        contact_table.add_column('Text', style='green')           

        for note in result:
            contact_table.add_row(str(note.ID), all_tag, note.title, note.text)

        console = Console()
        console.print(contact_table)
    
    
    def delete(self, id):
        for note in self.data:
            if note.ID == id:
                self.data.remove(note)
    
    def show_all_notes(self):
        
        contact_table = Table(title='All notes', show_lines=True, width=125)
        contact_table.add_column('ID', style='cyan')
        contact_table.add_column('Tag', style='magenta')
        contact_table.add_column('Title', style='yellow')
        contact_table.add_column('Text', style='green')           

        for note in self.data:
            all_tag = ''
            for tag in note.tag:
                all_tag = all_tag + ', ' + tag
                all_tag = all_tag.removeprefix(', ')
            contact_table.add_row(str(note.ID), all_tag, note.title, note.text)

        console = Console()
        console.print(contact_table)
    