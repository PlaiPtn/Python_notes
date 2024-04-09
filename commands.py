from workWithFile import workWithFile
import datetime
import json


class Commands:
    def __init__(self):
        self.json_data = workWithFile()
        self.__dict_commands = {1: "Создать новую заметку",
                                2: "Читать все заметки",
                                3: "Редактирование заметки",
                                4: "Удаление заметки"}

    def write_note(self):
        header = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        self.json_data.write_json(header, body)

    def read_notes(self):
        self.json_data.read_json()

    def edit_note(self):
        id = input("Введите Id заметки которую хотите изменить")

    def del_note(self):
        pass

    @property
    def get_dict_commands(self):
        return self.__dict_commands
