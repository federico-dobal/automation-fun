#!/usr/bin/python

import requests
import json

HEADERS = {'Content-Type': 'application/json'}

def execute_post(url, body):
    response = requests.post(
            url=url,
            headers=HEADERS,
            data=json.dumps(body, indent=4))

    # Ensure it has been created successfully
    if response.status_code != 200:
        raise Exception('Error executing POST')

    return (response.status_code, json.loads(response.text))

def execute_get(url):
    response = requests.get(
            headers=HEADERS,
            url=url)
    # Ensure it has been created successfully
    if response.status_code != 200:
        print(url)
        raise Exception('Error executing GET')

    return (response.status_code, json.loads(response.text))
