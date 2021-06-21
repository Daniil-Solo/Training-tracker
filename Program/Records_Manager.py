import json
import os


class RecordManager:
    def __init__(self):
        self.n_records = 0
        self.data_dict = dict()
        self.load_data()

    # функции-загрузчики
    def load_data(self):
        if os.path.exists('source/my_records.json'):
            with open("source/my_records.json", "r") as read_file:
                self.data_dict = json.load(read_file)
        else:
            with open('source/my_records.json', "w") as write_file:
                json.dump(self.data_dict, write_file)

    # функции для изменения значений
    def data_change(self, distance, time):
        self.data_dict[distance] = time

# функция сохранения
    def save_changes(self):
        with open('source/my_records.json', "w") as write_file:
            json.dump(self.data_dict, write_file)