import json
import os
from PIL import Image


class Profile:

    def __init__(self):

        self.data_dict = {
            'name': None,
            'gender': 0,
            'height': None,
            'weight': None,
            'birthday': None,

            'record_100': None,
            'record_200': None,
            'record_400': None,
            'record_800': None,
            'record_1_000': None,
            'record_3_000': None,
            'record_5_000': None,
            'record_10_000': None,
            'record_21_000': None,
            'record_42_000': None,
        }
        self.new_photo_adress = None
        self.need_saving = False

    def load_data(self):
        if os.path.exists('my_profile.json'):
            with open("my_profile.json", "r") as read_file:
                self.data_dict = json.load(read_file)
        else:
            with open('my_profile.json', "w") as write_file:
                json.dump(self.data_dict, write_file)
        return self.data_dict

    def data_change(self, key, value):
        self.need_saving = True
        self.data_dict[key] = value

    def photo_change(self, photo_adress):
        image = Image.open(photo_adress)
        size = (251, 261)
        out = image.resize(size)
        new_photo_adress = 'temp_my_photo.jpg'
        out.save(new_photo_adress, "JPEG")
        self.need_saving = True
        self.new_photo_adress = new_photo_adress
        return new_photo_adress

    def save_changes(self):
        if self.new_photo_adress is not None:
            image = Image.open(self.new_photo_adress)
            image.save("my_photo.jpg", "JPEG")
        with open('my_profile.json', "w") as write_file:
            json.dump(self.data_dict, write_file)
        self.need_saving = False
