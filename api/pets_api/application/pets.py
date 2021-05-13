#!/usr/bin/python

import argparse
from pets_helper import *
from user import *
from config import *

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser')

parser_user = subparsers.add_parser('user')
parser_user.add_argument(
    '-uname', '--uname', dest='uname', help='User name', required=True)
parser_user.add_argument(
    '-upassword', '--upassword', dest='upassword', help='User password', required=True)

parser_pets_details = subparsers.add_parser('pets_details')

parser_count_name = subparsers.add_parser('count_name')

kwargs = vars(parser.parse_args())

try:
    config = ConfigData()
    subcommand = kwargs.pop('subparser')

    if subcommand == 'user':
        print('Execute user')
        create_user(config.get_api_url(),
                    config.get_api_user_path(),
                    kwargs.get('uname'), kwargs.get('upassword'))

    if subcommand == 'pets_details':
        print('Execute pets_details')
        pets_by_id = get_pets_by_id(config.get_api_url(),
                                    config.get_api_pet_by_state_path())

        for pet in pets_by_id:
            print(pet)

    if subcommand == 'count_name':
        print('Execute count_name')
        pets_by_id = get_pets_by_id(config.get_api_url(),
                                    config.get_api_pet_by_state_path())
        pets_helper = PetsHelper(pets_by_id)
        number_pets_by_name = pets_helper.count_pets_by_name()
        print(number_pets_by_name)

    print('Command executed successfully')

except KeyError as e:
    print("Error: please provide a subcommand")
    print("Hint: execute python pets.py -h")
except Exception as e:
    print('Error: {}'.format(str(e)))