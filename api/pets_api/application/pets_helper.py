#!/usr/bin/python

from requests_helper import *
from pets_helper import *


def get_pets_by_id(pets_url, pet_by_state_path):
    get_url = "{}/{}".format(pets_url, pet_by_state_path)
    http_code, response_text = execute_get(get_url)

    if http_code != 200:
        print('Error obtaining pets by state', http_code)
        exit(0)

    return list(map(lambda pet: (pet.get('id'), pet.get('name')),
        filter(lambda pet: pet.get('name') != None and len(pet.get('name')) > 0, response_text)))


class PetsHelper():
    def __init__(self, pets):
        self.pets = pets

    def count_pets_by_name(self):
        pets_name = list(map(lambda x: x[1], self.pets))
        number_pets_by_name = dict((x,pets_name.count(x)) for x in set(pets_name))
        return {k: v for k, v in sorted(number_pets_by_name.items(), key=lambda item: -item[1])}
