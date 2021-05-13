import json
from requests_helper import *
from pets_helper import *

user_body = {
  'id': 0,
  'firstName': "test_api_fname",
  'lastName': "test_api_lname",
  'email': "a@a.com",
  'phone': "12345678",
  'userStatus': 0
}

def create_user(pets_url, user_path, username, password):
    user_body['username'] = username
    user_body['password'] = password
    # Create a new user
    post_url = "{}/{}".format(pets_url, user_path)
    http_code, response_text = execute_post(post_url, user_body)

    # Retrieve the user details
    get_url = "{}/{}/{}".format(pets_url, user_path, username)
    http_code, response_text = execute_get(get_url)
    print(response_text)


