import datetime
class ModelNotes:
    @property
    def get_note(self):
        return [input("Введите заголовок заметки: \n"), input("Введите текст заметки: \n"),
                str(datetime.datetime.now())]
