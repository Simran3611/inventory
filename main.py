import inventory
from tabulate import tabulate

answer = input("What would you like to do (insert, delete, update, retrieve, search): ")

if answer == "insert":
    item = input("Enter item name: ")
    description = input("Enter item description: ")
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")
    inventory.insert_items(item, description, price, quantity)

elif answer == "retrieve":
    items = inventory.retrieve_items()
    # headers = ["ID", "Item", "Description", "Price", "Quantity"]
    # table = tabulate(items, headers, tablefmt="grid")
    # print(table)

elif answer == "update":
    updateWhat = input("What would you like to update (item, description, price, quantity): ")
    itemID = input("Enter item id: ")
    if updateWhat == 'item':
        item = input("Enter item name: ")
        inventory.update_items(itemID, item)
    elif updateWhat == 'description':
        description = input("Enter item description: ")
        inventory.update_items(itemID, description)
    elif updateWhat == 'price':
        price = input("Enter item price: ")
        inventory.update_items(itemID, price)
    elif updateWhat == 'quantity':
        quantity = input("Enter item quantity: ")
        inventory.update_items(itemID, quantity)
    else:   
        print("Invalid option.")

elif answer == "delete":
    itemID = input("Enter item id: ")
    inventory.delete_items(itemID)

elif answer == "search":
    item = input("Enter item name: ")
    items = inventory.search_items(item)
    headers = ["ID", "Item", "Description", "Price", "Quantity"]
    table = tabulate(items, headers, tablefmt="grid")
    print(table)
