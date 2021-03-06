import json
import os


class RecordManager:
    def __init__(self):
        self.n_records = 0
        self.data_dict = dict()
        self.load_data()

    def delete_all(self):
        self.data_dict = {}

    # функции-загрузчики
    def load_data(self):
        if os.path.exists('./source/my_records.json'):
            with open("./source/my_records.json", "r") as read_file:
                self.data_dict = json.load(read_file)
        else:
            with open('./source/my_records.json', "w") as write_file:
                json.dump(self.data_dict, write_file)

    # функции для изменения значений
    def data_change(self, distance, time):
        self.data_dict[distance] = time

    # функция сохранения
    def save_changes(self):
        with open('./source/my_records.json', "w") as write_file:
            json.dump(self.data_dict, write_file)

    def get_list_records(self, order=True):
        list_records = []
        for key in self.data_dict:
            value = self.data_dict[key]
            item = (float(key), value)
            list_records.append(item)
        if order:
            list_records.sort(key=lambda x: x[0])
        return list_records
