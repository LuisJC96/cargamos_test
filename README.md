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
notice the database name will be taken from the configuratins.yaml file, by default it's name is "cargamos"

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

## Usage

To start the server run next command:

```bash
python3 server.py
```

## Endpoints
### /
The / endpoint it's simply connected to a whoami resource with the propouse to check connection
GET request 
```bash
"Hello from the store!!"
```
POST request
```bash
{
    "success": true,
    "args": {},
    "json": {
        "product_id": 1
    }
}
```
### /order
GET request example:
```bash
{
    "order_id":1
}
```
GET answer example:
```bash
{
    "success": true,
    "products": {
        "order_id": 1,
        "customer_id": 1,
        "store_id": 1,
        "order_date": "<class 'datetime.date'>",
        "customer_name": "John Doe",
        "customer_phone_number": "+525555555555",
        "customer_mail": "johndoe@test.com",
        "customer_street": "1st street",
        "customer_city": "1st City",
        "customer_state": "1st state",
        "customer_zip_code": "00000",
        "products": [
            {
                "product_id": 2,
                "quantity": 2,
                "product_unit": 70,
                "product_total_cost": 140.0,
                "prduct_name": "Book2"
            },
            {
                "product_id": 1,
                "quantity": 1,
                "product_unit": 91,
                "product_total_cost": 91.0,
                "prduct_name": "Book1"
            }
        ],
        "total_cost": 231.0
    }
}
```
POST request example:
```bash
{
    "customer_id":1,
    "store_id":1,
    "products":[
        {
            "product_id":2,
            "quantity":1
        }
    ]
}
```
POST answer example:
```bash
{
    "success": true
}
```
### /product
GET request example:
```bash
{
    "product_id":1
}
```
GET answer example:
```bash
{
    "success": true,
    "products": [
        {
            "product_id": 1,
            "product_name": "Book1",
            "product_description": "A Nice book1",
            "product_cost": 91
        }
    ]
}
```
POST request example:
```bash
{
    "product_name":"The maxi book",
    "product_description":"Its the maxi book",
    "product_cost":521
}
```
POST answer example:
```bash
{
    "success": true,
    "product": {
        "product_name": "The maxi book",
        "product_description": "Its the maxi book",
        "product_cost": 521
    }
}
```
PUT request example:
Only variables which wished to be updated
```bash
{
    "product_id":60,
    "product_name":"The Mega maxi book",
    "product_cost":550
}
```
PUT answer example:
```bash
{
    "success": true,
    "product": {
        "product_id": 60,
        "product_name": "The Mega maxi book",
        "product_cost": 550
    }
}
```
### /inventory
GET request example:
notice that deoending on the variables given the endpoint will asnwer differently:
if you send store_id it will return the complete inventory of the store
if you send product_id it will return the inventory of that product accross all the stores
if you send product_id and store_id it will only return the inventory of an specific product on an specific store
as well if the json is null it will return all the inventory accross all the stores:

GET answer example:
```bash
{
    "success": true,
    "inventory": {
        "1": {
            "store_name": "I completely love books",
            "store_inventory": [
                {
                    "Book2": 1
                },
                {
                    "Book3": 1
                },
                {
                    "Book4": 1
                },
                {
                    "Book5": 1
                },
                {
                    "Book6": 200
                },
                {
                    "Book1": 10
                }
            ]
        },
        "2": {
            "store_name": "I sell books",
            "store_inventory": [
                {
                    "Book1": 2
                },
                {
                    "Book2": 2
                },
                {
                    "Book3": 2
                },
                {
                    "Book4": 2
                },
                {
                    "Book5": 2
                }
            ]
        },
        "3": {
            "store_name": "Books for everyone",
            "store_inventory": [
                {
                    "Book1": 3
                },
                {
                    "Book2": 3
                },
                {
                    "Book3": 3
                },
                {
                    "Book4": 3
                },
                {
                    "Book5": 3
                }
            ]
        }
    }
}
```
### /modify_stock

adds or deminishes x quantity of the given product on the given store
POST request example:
```bash
{
    "store_id":1,
    "product_id":60,
    "quantity":25
}
```
POST answer example:
```bash
{
    "success": true
}
```
