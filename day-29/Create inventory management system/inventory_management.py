inventory = {}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        inventory[name] = qty
        print("Product Added")

    elif ch == 2:
        print("Products in Inventory:")
        for i in inventory:
            print(i, ":", inventory[i])

    elif ch == 3:
        name = input("Enter product name to search: ")
        if name in inventory:
            print("Quantity =", inventory[name])
        else:
            print("Product Not Found")

    elif ch == 4:
        name = input("Enter product name to delete: ")
        if name in inventory:
            del inventory[name]
            print("Product Deleted")
        else:
            print("Product Not Found")

    elif ch == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")