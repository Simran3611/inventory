import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="temp"
)


def insert_items(item, description, price, quantity):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Inventory")
    result = mycursor.fetchall()
    for row in result:
        if row[1] == item:
            print("Item already exists")
            break
    else:
        mycursor.execute("INSERT INTO Inventory (item, description, price, quantity) VALUES (%s, %s, %s, %s)",
                          (item, description, price, quantity))
        db.commit()
        print("Item added successfully")
    mycursor.close()

def retrieve_items():
    # mycursor = db.cursor()
    # mycursor.execute("SELECT * FROM Inventory")
    # for x in mycursor:
    #     print(x)
    # mycursor.close()
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
        for row in result:
            print("Item ID:", row[0])
            print("Item Name:", row[1])
            print("Description:", row[2])
            print("Price:", row[3])
            print("Quantity:", row[4])
    mycursor.close()

