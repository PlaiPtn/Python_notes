from workWithFile import WorkWithFile
from modelNotes import ModelNotes


class Commands:

    def __init__(self):
        self._modelNotesh = ModelNotes()
        self._json_file = WorkWithFile()
        self._json_data = self._json_file.get_data()
        self._json_last_id = self._json_file.get_last_id()
        self._dict_commands = {1: ["Создать новую заметку", self._write_note],
                                2: ["Читать все заметки", self._read_notes],
                                3: ["Редактирование заметки", self._edit_note],
                                4: ["Удаление заметки", self._del_note],
                                5: ["Выход из программы", self._exit]}


    def input_com(self, command):
        self._dict_commands[command][1]()

    def _write_note(self):
        self._json_last_id += 1
        note = self._modelNotesh.get_note
        self._json_data |= {self._json_last_id: note}
        self._json_file.write_json(self._json_data)

        return "Запись создана"

    def _read_notes(self):
        for k, v in self._json_data.items():
            print(f"id = {k}")
            print(f"Заголовок = {v[0]}")
            print(f"Текст = {v[1]}")
            print(f"Дата изменения = {v[2]}")
        return "Список заметок выведен"

    def _edit_note(self):
        id = input("Введите Id заметки которую хотите изменить\n")
        note = self._modelNotesh.get_note
        self._json_data[id] = note
        self._json_file.write_json(self._json_data)
        return f"Заметка c id {id} изменена"

    def _del_note(self):
        id = input("Введите Id заметки которую нужно удалить\n")
        del self._json_data[id]
        return f"Заметка c id {id} удалена"

    def _exit(self):

        return False;

    @property
    def get_dict_commands(self):
        return self._dict_commands
