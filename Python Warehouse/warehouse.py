""" 

Program: Warehouse control system
Functionality:
    1    - register new items on the system
        * id (auto generate)
        * title
        * category
        * price
        * stock
    2   - list the items on the systems
    3   - updte quantity on stock for a selected item
    4   - list items with stock (stock > 0)

    """
import sys
from menu import print_menu
from item import Item

import pickle

import os
clear = lambda: os.system('cls')

item_list = []
event_log = []
id_count = 1
items_file = "items.data"  #files are good for testing, but not for production
log_file = "log.data"

#def clear():
#    print("\033[H\033[J")

def save_items():
    try:
        writer = open(items_file, "wb") #wb writer binary information
        pickle.dump(item_list, writer)
        writer.close()
        print("Data saved")
    
    except:
        print("**Error: Data could not be saved")


def read_items():
    global id_count
    global items_file

    try:
        reader = open(items_file, "rb") #read binary
        temp_data = pickle.load(reader)

        for item in temp_data:
            item_list.append(item)

        last = item_list[-1]
        id_count = last.id + 1

        print("Data loaded: " + str(len(item_list)) + " items ")
    
    except:
        print("**Error: Data could not be loaded")


def read_events():
    global log_file

    try:
        reader = open(log_file, "rb") #read binary
        temp_data = pickle.load(reader)

        for event in temp_data:
            event_log.append(event)

        print("Events loaded")
    
    except:
        print("**Error: Log events could not be loaded")

def save_log():
    try:
        writer = open(log_file, "wb") #wb writer binary information
        pickle.dump(event_log, writer)
        writer.close()
        print("Log saved")
    
    except:
        print("**Error: Log could not be saved")


def remove_item():
    #print("\n\n\n\n")
    print("*" * 40)
    print("Remove an item")
    print("*" * 40)
    item = select_item()
    if(item is not None):
        item_list.remove(item)
        print("Item removed")

def log_events():
    #print("\n\n\n\n")
    print("*" * 40)
    print("Event logs")
    print("*" * 40)
    for event in event_log:
        print(event)



def stock_value():
    #print("\n\n\n\n")
    print("*" * 40)
    print("Stock Value")
    print("*" * 40)
    total = 0
    for item in item_list:
        val = item.price * item.stock
        total +=val 

    print("The total value of the stock is: " + str(total))

    if(len(item_list) < 1):
        print(" - Empty database, please use option 1 to create items - ")    
    print("*" * 40)

def register_item():
    global id_count
    try:
        #print("\n\n\n\n")
        print("*" * 40)
        print("Register an item")
        print("*" * 40)
        id = id_count
        title = input("Title: ")
        category = ("Category: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        new_item = Item(id, title, category, price, stock)

        item_list.append(new_item)
        id_count +=1
        print(len(item_list))

    except:
        print("***Error, please verify information and try again")
        print("**Error:" , sys.exc_info()[0])

def list_all():
    #print("\n\n\n\n")
    print("*" * 40)
    print("List of all items")
    print("*" * 40)
    for item in item_list:
        print(str(item.id) + " - " + format_left(20, item.title) + item.title + " $" + str(item.price) + " " + str(item.stock))

    if(len(item_list) < 1):
        print(" - Empty database, please use option 1 to create items - ")    
    print("*" * 40)

def list_with_stock():
    #print("\n\n\n\n")
    print("*" * 40)
    print("List of items with stock")
    print("*" * 40)
    for item in item_list:
        if(item.stock > 0):
            print(str(item.id) + " - " + format_left(20, item.title) + item.title + " $" + str(item.price) + " " + str(item.stock))

    if(len(item_list) < 1):
        print(" - Empty database, please use option 1 to create items - ")    
    print("*" * 40)

def update_stock():
    #print("\n\n\n\n")
    print("*" * 40)
    print("Updated Stock")
    print("*" * 40)
    item = select_item()
    if(item is not None):
        try:
            new_stock = int(input("Please provide new Stock value: "))
            item.stock = new_stock
            print("Status: Stock value updated")
        # ask for new stock value
        # assign the stock to the item
        except:
            print("Error! Stock should be a number, try again")

# action 1 - input
# action 2 - output
def register_entry(action):
        #print("\n\n\n\n")
        print("*" * 40)
        print("Stock")
        print("*" * 40)
        item = select_item()
        how_many = int(input("How many items: "))
        if(item is not None):
            
            if(action == 1):
                item.stock += how_many
                event = str(item.id) + " " + str(how_many) + " input"
                event_log.append(event)
            elif(action == 2):
                item.stock -= how_many
                event = str(item.id) + " " + str(how_many) + " output"
                event_log.append(event)

            save_log()
            print(" !! Entry successful !! ")

def select_item():
    list_all()
    try:
        selection = int(input("Id of item: "))
        for item in item_list:
            if(item.id == selection):
                return item
    except:
        print("ID should be a number, try again")

    #not found
    print(" *Error: ID not found, check and try again")
    return None


def format_left(how_many, text):
    if(len(text) == how_many):
        return text

    #cut the text (substring)
    if(len(text) > how_many):
        return text[0:how_many]

    while(len(text) < how_many):
        text = text + " "

    return text


# First thing is to read previous data
read_items()
read_events()

opc = ''
while (opc != 'x'):
    clear()
    print_menu()
    opc = input("Select an option: ")
    clear()

    if(opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        list_all()
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "4"):
        list_with_stock()
    elif(opc == "5"):
        remove_item()
        save_items()
    elif(opc == "6"):
        register_entry(1)
        save_items()
    elif(opc == "7"):
        register_entry(2)
        save_items()
    elif(opc == "8"):
        log_events()
    elif(opc == "9"): 
        stock_value()

    if(opc != 'x'):
        input("\n\nPress Enter to continue")

print("Thank you, goodbye!")


