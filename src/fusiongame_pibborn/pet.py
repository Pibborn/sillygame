import json

class Pet:
    def __init__(self, i, name, petclass):
        self.name = name
        self.petclass = petclass
        self.id = i

    def __str__(self):
        res = "{};Pet {} of class {}".format(self.id, self.name, self.petclass)
        return res

def load_from_file(path):
    with open(path, 'r') as file:
        json_data_list = json.load(file)
    pets = [Pet(**pet_data) for pet_data in json_data_list]
    return pets
