from control import *

class View:
    def __init__(self):
        self.dict_commands = get_commands()

    def run(self):
        while True:
            print()
            print("----------------------")
            print("Список команд:")
            for k, v in self.dict_commands.items():
                print(f"{k} - {v[0]}")
            print("----------------------")
            inp_com = input("Введите номер команды для работы или Q для выхода:\n")
            if inp_com.lower() == "q":
                print("До новых встреч!")
                return
            elif inp_com in self.dict_commands.keys():
                print(input_command(inp_com))
            else:
                print("Такой команды нет, попробуйте еще раз")

