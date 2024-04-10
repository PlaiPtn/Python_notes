import json
import os

class WorkWithFile:
    def __init__(self):
        if os.path.exists("notesData/notes_book.json"):
            with open("notesData/notes_book.json", 'r') as fp:
                self._data = json.load(fp)
            self._last_id = int(list(self._data)[-1])
        else:
            self._data = {}
            self._last_id = 0

    def write_json(self, dict_nodes):
        with open("notesData/notes_book.json", 'w', encoding="utf-8", ) as file:
            json.dump(dict_nodes, file)

    def get_data(self):
        return self._data
    def get_last_id(self):
        return self._last_id