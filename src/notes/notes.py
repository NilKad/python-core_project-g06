

class Note:
    # Для того, щоб вірно додати тег, потрібно попросити користувача вводити теги через пробіл в форматі "#tag #tag"
    def __init__(self, title, text):
        self.tag = 'No tag`s'
        self.title = title
        self.text = text
    
    def add_tag(self, tag):
    #Якщо користувач пропустить знак '#' під час введення, програма автоматично його додасть
        self.tag = tag.split(' ')
        for elem in self.tag:
            if elem[0] != '#':
                tags_elem = '#' + elem
                self.tag.remove(elem)
                self.tag.insert(0, tags_elem)

    def edit_tag(self, new_tag):
        self.tag = new_tag.split(' ')
        for elem in self.tag:
            if elem[0] != '#':
                tags_elem = '#' + elem
                self.tag.remove(elem)
                self.tag.insert(0, tags_elem)
    
    def edit_title(self, new_title):
        self.title = new_title

    def edit_text(self, new_text):
        self.text = new_text

    def __str__(self):
        return f'Tag: {self.tag}\nTitle: {self.title}\nText: {self.text}'
    
    
    


            

book = Notebook()
new_note = Note('Modern Buildins', 'Modern buildings showcase a wide range of architectural styles, \ntechnologies, and sustainable design practices.')
new_note.add_tag('buildings architecture #design, art')

second_note = Note('Salvador Dali', 'Dalí was a leading figure in the Surrealist movement, \nwhich sought to unlock the creative potential of the unconscious mind.')
second_note.add_tag('art #surrealism')

book.add_note(new_note)
book.add_note(second_note)

print(book.find_by_tag('#art'))
print(book.sort_by_tag())

