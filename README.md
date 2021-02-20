# Cargamos Test

This is the cargamos test Repository

## Installation

fist create a user on your previously installed postgresql instance with the command:
```bash
create --interactive --pwprompt
```
On the configurations.yaml the defalut user and password are root and root respectively

After creating the user run the command: 

```bash
pip3 install -r requirements.txt
```
to install all the dependencies

If everything is correctly set up you can run the file process_create_database.py located in the processes folder
with:
```bash
python3 process_create_database.py
```
Which will create the database with all the core needed tables

finally you can run the process_insert_demo_values_into_db.py located also in the processes folder
```bash
python3 process_insert_demo_values_into_db.py
```

Which will insert some demo values into the db

As an extra i created the orders table which in my opinion was needed to complement the functionality of this system

## Tests

The test are located on the tests folder and can be used with the command:

```bash
pytest-3
```
