import json_structure


class Commands:
    def __init__(self):
        self.__dict_commands = {1: ["Создать новую заметку", self.record_note],
                                2: ["Читать все заметки", self.read_notes],
                                3: ["Редактирование заметки", self.edit_note],
                                4: ["Удаление заметки", self.del_note]}

    def record_note(self):
        print(1111)

    def read_notes(self):
        pass

    def edit_note(self):
        pass

    def del_note(self):
        pass

    @property
    def dict_commands(self):
        return self.__dict_commands
