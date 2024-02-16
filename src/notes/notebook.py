from collections import UserDict


class Notebook(UserDict):
    id = 1
    def add_note(self, note):
        self.data[self.id] = note
        self.id += 1

    def find_by_tag(self, tag):
        #Повертає список заголовків статей по заданому тегу
        result = []
        for note in self.data.values():
            if tag in note.tag:
                result.append(note.title)
        return result
    
    def sort_by_tag(self):
        #Повертає словник з де ключ це тег, а значення список із статей в яких він є
        result = {}
        for note in self.data.values():
            for tag in note.tag:
                if tag not in result.keys():
                    result[tag] = [note.title]
                else:
                    result[tag].append(note.title)
        return result
            
    def find_by_id(self, id):
        return self.data.get(id)

    def find_by_title(self, title):
        for note in self.data.values():
            if note.title == title:
                return note
    
    def delete(self, id_or_title):
        #Функція видаляє по ID або по назві записки
        for id, note in self.data.items():
            if id == id_or_title:
                self.data.pop(id)
                break
            if note.title == id_or_title:
                self.data.pop(id)
                break
    
    def show_all_notes(self):
        #Костиль виводу всіх записок 
        print('|{:^10}|{:^30}|{:^30}|'.format('ID', "TEG", "TITLE"))
        for id, note in self.data.items():
            print('|{:^10}|{:^30}|{:^30}|'.format(id, note.tag[0], note.title))
            
    
    