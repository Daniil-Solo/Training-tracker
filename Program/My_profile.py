import json
import os
from PIL import Image


class Profile:

    def __init__(self):

        self.data_dict = {
            'name': None,
            'gender': 0,
            'weight': None,
            'birthday': None,

            'photo_path': 'source/default_photo.jpg',

            'nice_days': 0,
            'goal':
                {
                    'title': None,
                    'type': None,
                    'values': None
                },

            'raiting_app': 0

        }
        self.load_data()
        self.set_photo()

# примитивные функции
    def get_data_dict(self):
        return self.data_dict

    def get_photo_path(self):
        return self.data_dict['photo_path']

# функции для изменения значений
    def data_change(self, key, value):
        self.data_dict[key] = value

    def photo_change(self, photo_adress):
        image = Image.open(photo_adress)
        old_width, old_height = image.size
        new_size = (251, 261)
        if old_width > old_height:
            new_width = int((old_height / new_size[1]) * new_size[0])
            new_height = old_height
        else:
            new_height = int((old_width / new_size[0]) * new_size[1])
            new_width = old_width

        out_image = image.crop(((old_width-new_width)//2, (old_height-new_height)//2,
                               (old_width+new_width)//2, (old_height+new_height)//2))

        out_image = out_image.resize(new_size)
        self.data_change('photo_path', 'source/my_photo.jpg')
        out_image.save(self.get_photo_path(), "JPEG")

# функции-загрузчики
    def load_data(self):
        if os.path.exists('source/my_profile.json'):
            with open("source/my_profile.json", "r") as read_file:
                self.data_dict = json.load(read_file)
        else:
            with open('source/my_profile.json', "w") as write_file:
                json.dump(self.data_dict, write_file)

    def set_photo(self):
        if os.path.exists(self.get_photo_path()):
            pass
        elif os.path.exists('source/default_photo.jpg'):
            self.data_change('photo_path', 'source/default_photo.jpg')
        else:
            self.data_change('photo_path', None)

# функция сохранения
    def save_changes(self):
        with open('source/my_profile.json', "w") as write_file:
            json.dump(self.data_dict, write_file)
