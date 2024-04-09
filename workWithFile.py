
import json
import os

class workWithFile:
    def __init__(self):
        if os.path.exists("notesData/notes_book.json"):
            with open("notesData/notes_book.json", 'r') as fp:
                self.data = json.load(fp)
            self.last_id = int(list(self.data)[-1])
        else:
            self.data = {}
            self.last_id = 0

    def write_json(self, header, body):
        temp_dict = self.data | {self.last_id + 1: [header, body, self.date]}
        with open("notesData/notes_book.json", 'w') as file:
            json.dump(temp_dict, file)

    def read_json(self):
        for k, v in self.data.items():
            print(f"id = {k}")
            print(f"Заголовок = {v[0]}")
            print(f"Текст = {v[1]}")
            print(f"Дата изменения = {v[2]}")

    def edit_json(self, id):