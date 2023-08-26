import mysql.connector
from tabulate import tabulate


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="temp"
)

mycursor = db.cursor()
mycursor.execute(
    "CREATE DATABASE IF NOT EXISTS temp"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Inventory (item VARCHAR(255), Description VARCHAR(255), Price DECIMAL(6,3), Quantity INT, PLUnumber INT)"
)
import sys
def read_barcode():
    try:
        while True:
            PLUnumber = input("Scan a barcode (press 'q' to quit): ")
            if PLUnumber.lower() == 'q':
                break
            item = input("Enter item name: ")
            description = input("Enter description: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")

            # Insert data into the database
            insert_items(item, description, price, quantity, PLUnumber)

            print("Scanned Data (PLUnumber):", PLUnumber)
    except KeyboardInterrupt:
        print("Barcode scanning stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

#once insert works, modify according to the task
#delete this after!!! or modify
# def read_barcode():
#     try:
#         while True:
#             barcode_data = input("Scan a barcode (press 'q' to quit): ")
#             if barcode_data.lower() == 'q':
#                 break
#             # print("Scanned Data:", barcode_data)
#             return(barcode_data)
#     except KeyboardInterrupt:
#         print("Barcode scanning stopped.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     if sys.platform != "win32":
#         print("This script is designed for Windows OS.")
#         sys.exit(1)
    
#     print("Barcode scanner script (press 'q' to quit)")
    

def insert_items(item, description, price, quantity, PLUnumber):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Inventory")
    result = mycursor.fetchall()
    for row in result:
        if row[1] == item:
            print("Item already exists")
            break
    else:
        # PLUnumber = read_barcode()
        mycursor.execute("INSERT INTO Inventory (item, description, price, quantity, PLUnumber) VALUES (%s, %s, %s, %s, %s)",
                 (item, description, price, quantity, PLUnumber))

        db.commit()
        print("Item added successfully")
    mycursor.close()
    

def retrieve_items():   
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Inventory")
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Inventory is empty")
    else:
        headers = ["ID", "Item", "Description", "Price", "Quantity"]
        print(tabulate(result, headers, tablefmt="pretty"))
    mycursor.close()

def update_items(itemID, item=None, description=None, price=None, quantity=None):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Inventory WHERE id = %s", (itemID,))
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Item does not exist")
    else:
        if item is not None:
            mycursor.execute("UPDATE Inventory SET item = %s WHERE id = %s",
                              (item, itemID))
        if description is not None:
            mycursor.execute("UPDATE Inventory SET description = %s WHERE id = %s",
                              (description, itemID))
        if price is not None:
            mycursor.execute("UPDATE Inventory SET price = %s WHERE id = %s",
                              (price, itemID))
        if quantity is not None:
            mycursor.execute("UPDATE Inventory SET quantity = %s WHERE id = %s",
                              (quantity, itemID))
        db.commit()
        print("Item updated successfully")
    mycursor.close()

def delete_items(itemID):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Inventory WHERE id = %s", (itemID,))
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Item does not exist")
    else:
        mycursor.execute("DELETE FROM Inventory WHERE id = %s", (itemID,))
        db.commit()
        print("Item deleted successfully")
    mycursor.close()

def search_items(search_item):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Inventory WHERE item LIKE %s", ('%' + search_item + '%',))
    result = mycursor.fetchall()
    if len(result) == 0:
        print("No items found")
        
    else:
        headers = ["ID", "Item", "Description", "Price", "Quantity"]
        print(tabulate(result, headers, tablefmt="pretty"))
        # for row in result:
            # print("Item ID:", row[0])
            # print("Item Name:", row[1])
            # print("Description:", row[2])
            # print("Price:", row[3])
            # print("Quantity:", row[4])
    mycursor.close()

