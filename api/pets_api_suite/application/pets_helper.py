from requests_helper import *
from pets_helper import *
# TODO: receive parameters from properties file
PET_BY_STATE_PATH = 'pet/findByStatus?status=available&status=pending&status=sold'
PETS_URL = "https://petstore.swagger.io/v2"


def get_pets_by_id():
    get_url = "{}/{}".format(PETS_URL, PET_BY_STATE_PATH)
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
