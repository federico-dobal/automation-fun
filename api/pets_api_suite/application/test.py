import pytest
from pets_helper import *

pets_by_id = [
    (9222968140498509266, 'doggie'),
    (9222968140498509267, 'doggie'),
    (9222968140498509272, 'fish'),
    (9222968140498509273, 'doggie'),
    (1, 'doggie'),
    (9222968140498509278, 'fish'),
    (9222968140498509280, 'fish')
]

def test_count_pets_non_empty_success():
    # GIVEN a non empty list of pets
    pets_helper = PetsHelper(pets_by_id)

    # WHEN the number of pets by name are required
    number_pets_by_name = pets_helper.count_pets_by_name()

    # THEN: the pets are counted properly
    assert len(number_pets_by_name) == 2

    assert number_pets_by_name.get('doggie') == 4
    assert number_pets_by_name.get('fish') == 3

def test_count_pets_empty_success():
    # GIVEN a non empty list of pets
    pets_helper = PetsHelper([])

    # WHEN the number of pets by name are required
    number_pets_by_name = pets_helper.count_pets_by_name()

    # THEN: the pets are counted properly
    assert len(number_pets_by_name) == 0