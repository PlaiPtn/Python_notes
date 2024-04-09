import datetime
class modelNotes:
    def __init__(self):
        self.header = input("Введите заголовок заметки")
        self.body = input("Введите текст заметки")
        self.date = datetime.datetime.now()

    @property
    def get_note(self):
        return [self.header, self.body, self.date]
