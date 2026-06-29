a = []

while True:
    print("\n--- Array Menu ---")
    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        x = int(input("Enter element: "))
        a.append(x)
        print("Element Inserted")

    elif ch == 2:
        print("Array =", a)

    elif ch == 3:
        x = int(input("Enter element to search: "))
        if x in a:
            print("Element Found")
        else:
            print("Element Not Found")

    elif ch == 4:
        x = int(input("Enter element to delete: "))
        if x in a:
            a.remove(x)
            print("Element Deleted")
        else:
            print("Element Not Found")

    elif ch == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")