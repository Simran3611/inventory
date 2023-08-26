import inventory
from tabulate import tabulate
#import libraries

    
answer = input("What would you like to do (insert, delete, update, retrieve, search): ")

if answer == "insert":
    #delete this after!!!!
    # item = input("Enter item name: ")
    # description = input("Enter item description: ")
    # price = input("Enter item price: ")
    # quantity = input("Enter item quantity: ")
    # inventory.insert_items(item, description, price, quantity)
    inventory.read_barcode()

elif answer == "retrieve":
    inventory.retrieve_items()
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
    inventory.search_items(item)
    # print(table)
