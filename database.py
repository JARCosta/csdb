import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
import server
import os
import csv
import json


def print_function_info(func):
    def wrapper(*args, **kwargs):
        filename = os.path.abspath(__file__)
        line_number = func.__code__.co_firstlineno + 1
        print(f"I am in {filename}:{line_number} in {func.__name__}")
        return func(*args, **kwargs)
    return wrapper




@print_function_info
def get_user_list():

    with open('memory/users.json', 'r') as f:
        users = json.load(f)

    return users

@print_function_info
def set_user_list(users: list[dict]):

    with open('memory/users.json', 'w') as f:
        json.dump(users, f, indent=2)

    return

@print_function_info
def add_user(user: dict):

    users = get_user_list()
    users.append(user)

    with open('memory/users.json', 'w') as f:
        json.dump(users, f, indent=2)

    return



@print_function_info
def get_users_db():
    return get_user_list()




@print_function_info
def get_inventory_price(steamid: str):
    return


@print_function_info
def get_inventory_size(steamid: str):
    return


@print_function_info
def get_inventory_unique_items_size(steamid: str):
    return


@print_function_info
def create_item(item_name: str, item_type: str):
    return


@print_function_info
def get_items():
    return

@print_function_info
def get_item_list():
    
    users = get_user_list()

    items = []

    for user in users:
        try :
            with open(f"memory/inventory/{user['steamid']}.json", 'r') as f:
                inventory = json.load(f)
            for item in inventory:
                if item not in items:
                    items.append(item)
        except FileNotFoundError:
            pass

    return items


@print_function_info
def set_item_price(item_name: str, price: int, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
    return



@print_function_info
def add_to_inventory(steamid: str, item_name: str, quantity: int, auto: bool):
    return


@print_function_info
def alter_item(steamid, item, quantity):
    return


#--------------------------------------------------------------
#-- Inventory -------------------------------------------------
#--------------------------------------------------------------

@print_function_info
def get_inventory(steamid: str):
    
    with open(f"memory/inventory/{steamid}.json", 'r') as f:
        inventory = json.load(f)
    
    return inventory


@print_function_info
def set_inventory(steamid: str, inventory: dict):
    
    with open(f"memory/inventory/{steamid}.json", 'w') as f:
        json.dump(inventory, f, indent=2)

    return


@print_function_info
def clear_auto_inventory(steamid: str):
    return


@print_function_info
def get_items_to_update():
    return


@print_function_info
def get_latest_prices():
    return


@print_function_info
def profile_items():
    return


@print_function_info
def delete_item(item_name: str):
    return


