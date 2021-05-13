import json
from requests_helper import *
from pets_helper import *

USER_PATH = "user"

user_body = {
  'id': 0,
  'firstName': "test_api_fname",
  'lastName': "test_api_lname",
  'email': "a@a.com",
  'phone': "12345678",
  'userStatus': 0
}

def create_user(username, password):
    user_body['username'] = username
    user_body['password'] = password
    # Create a new user
    post_url = "{}/{}".format(PETS_URL, USER_PATH)
    http_code, response_text = execute_post(post_url, user_body)

    # Retrieve the user details
    get_url = "{}/{}/{}".format(PETS_URL, USER_PATH, username)
    http_code, response_text = execute_get(get_url)
    print(response_text)


