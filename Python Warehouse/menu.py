import datetime

def get_date_time():
    current = datetime.datetime.now()
    time = current.strftime("%c")
    return time

def print_menu():
    #print("\n\n\n\n")
    print("*" * 60)
    print("Warehouse Control System        " + get_date_time())
    print("*" * 60)
    print("[1] Register new item")
    print("[2] List of items")
    print("[3] Update stock")
    print("[4] Updated stock list")
    print("[5] Remove item from the system")
    print("[6] Register an entry")
    print("[7] Register a sold item(s)")
    print("[8] See log of events")
    print("[9] Stock Value")


    print("[x] Exit the system")