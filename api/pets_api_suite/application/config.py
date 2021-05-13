import configparser

class ConfigData:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config/ConfigFile.properties')

        self.api_url = config.get('PetsSection', 'api.url')
        self.api_user_path = config.get('PetsSection', 'api.user_path')
        self.api_pet_by_state_path = config.get('PetsSection', 'api.pet_by_state_path')

    def get_api_url(self):
        return self.api_url

    def get_api_user_path(self):
        return self.api_user_path

    def get_api_pet_by_state_path(self):
        return self.api_pet_by_state_path
