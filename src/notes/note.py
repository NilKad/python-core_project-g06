# from Notes import Notes


class Note:
    # Для того, щоб вірно додати тег, потрібно попросити користувача вводити теги через пробіл в форматі "#tag #tag"
    def __init__(self, args):
        for key, value in args.items():
            # print(el)
            self.__setattr__(key, value)
            # self.__setattr__(key, value)

        # self.tag = ['No tag`s']
        # self.subject = subject
        # self.content = content
        # self.ID = None

    def update_all(self, args):
        if "id" in args:
            args.pop("id")
        # print()
        for key, value in args.items():
            self.__setattr__(key, value)
        return self

    def add_tag(self, tag):
        if self.tag == ["No tag`s"]:
            self.tag = tag.split(" ")
        else:
            self.tag.append(tag)

    def edit_tag(self, new_tag):
        self.tag = new_tag.split(" ")

    def edit_title(self, new_subject):
        self.subject = new_subject

    def edit_text(self, new_content):
        self.content = new_content

    def __str__(self):
        return f"id: {self.id}\tTags: {self.tags}\tsubject: {self.subject}\tContent: {self.content}"


# book = Notes()
# note1 = Note('Modern Buildings', 'Modern buildings showcase a wide range of architectural styles, technologies, and sustainable design practices.')
# note1.add_tag('buildings architecture #design')

# note2 = Note('Salvador Dali', 'Dalí was a leading figure in the Surrealist movement, \nwhich sought to unlock the creative potential of the unconscious mind.')
# note2.add_tag('#art')
# note2.add_tag('art2')

# note3 = Note('New Inventions', 'Explore the latest inventions and technological advancements that are shaping the future.')
# note3.add_tag('technology #innovation')

# note4 = Note('Historical Events', 'Discover key events that shaped the course of history and influenced societies around the world.')
# note4.add_tag('history #events')

# note5 = Note('Space Exploration', 'Delve into the mysteries of outer space and learn about the latest discoveries in space exploration.')
# note5.add_tag('space #science')
# note5.edit_tag('moonshine')

# note6 = Note('Nature Photography', 'Experience the beauty of nature through stunning photography capturing landscapes, wildlife, and more.')
# note6.add_tag('nature #photography #art')

# book.add_note(note1)
# book.add_note(note2)
# book.add_note(note3)
# book.add_note(note4)
# book.add_note(note5)
# book.add_note(note6)


# book.show_all_notes()
# book.find_by_tag('history')
# book.find_by_id(5)
# book.find_by_subject('Nature Photography')
# book.sort_by_tag()
