# Pet store

## Features
This project is compossed of the following features:

- Create a user and retrieve the details
- List the list of pets by status. States listed:
   - available
   - pending
   - sold
- Count the number of pets by name: particularly the output is sorted in decreasing order by the number of occurrences.

## How to set up the application?
It is required to create a new virtual environment and install the dependencies:

       virtualenv api_fun_venv
       source api_fun_venv/bin/activate
       pip install -r requirements.txt

## How to execute the application?
In order to execute it user should be placed under application/ directory:

       cd pets_api_suite/application

### User creation:

        python pets.py user -uname test -upassword admin123

### List the list of pets by status:

        python pets.py pets_details

### Count the number of pets by name

        python pets.py count_name   
        
        
## How to execute the tests?

       pytest test.py             
