import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="temp"
)

mycursor = db.cursor()

# Execute the CREATE TABLE query
mycursor.execute("CREATE TABLE IF NOT EXISTS Inventory ("
                 "id INT AUTO_INCREMENT PRIMARY KEY,"
                 "item VARCHAR(30) NOT NULL,"
                 "description VARCHAR(300) NOT NULL,"
                 "price DECIMAL(8,2) NOT NULL,"
                 "quantity INT(140) NOT NULL"
                 ")")

answer = input("What would you like to do (insert, delete, update, retrieve): ")

if answer == "insert":
    # Get the item details from the user
    item = input("Enter item name: ")
    description = input("Enter item description: ")
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")

    # Check if the item already exists in the table
    mycursor.execute("SELECT * FROM Inventory")
    result = mycursor.fetchall()
    for row in result:
        if row[1] == item:
            print("Item already exists")
            break
    else:
        # Add the item to the table
        mycursor.execute("INSERT INTO Inventory (item, description, price, quantity) VALUES (%s, %s, %s, %s)",
                          (item, description, price, quantity))
        db.commit()
        print("Item added successfully")

elif answer == "retrieve":
    # Display the contents of the Inventory table
    mycursor.execute("SELECT * FROM Inventory")
    for x in mycursor:
        print(x)

elif answer == "update":
    # Get the item details from the user
    itemID = input("Enter item id: ")
    mycursor.execute("SELECT * FROM Inventory WHERE id = %s", (itemID,))
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Item does not exist")
    else:
        item = input("Enter item name: ")
        description = input("Enter item description: ")
        price = input("Enter item price: ")
        quantity = input("Enter item quantity: ")
        column = input("Enter column to update (item, description, price, quantity): ")
        if column == "item":
            mycursor.execute("UPDATE Inventory SET item = %s WHERE id = %s",
                              (item, itemID))
        elif column == "description":
            mycursor.execute("UPDATE Inventory SET description = %s WHERE id = %s",
                              (description, itemID))
        elif column == "price":
            mycursor.execute("UPDATE Inventory SET price = %s WHERE id = %s",
                              (price, itemID))
        elif column == "quantity":
            mycursor.execute("UPDATE Inventory SET quantity = %s WHERE id = %s",
                              (quantity, itemID))
        else:
            print("Invalid column")
        db.commit()
        print("Item updated successfully")

elif answer == "delete":
    # Get the item details from the user
    itemID = input("Enter item id: ")
    mycursor.execute("SELECT * FROM Inventory WHERE id = %s", (itemID,))
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Item does not exist")
    else:
        mycursor.execute("DELETE FROM Inventory WHERE id = %s", (itemID,))
        db.commit()
        print("Item deleted successfully")

else:
    print("Invalid input")

# Close the cursor and database connection
mycursor.close()
db.close()
