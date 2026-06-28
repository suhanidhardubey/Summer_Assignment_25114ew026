contacts = {}

while True:
    print("\n1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        num = input("Enter number: ")
        contacts[name] = num
        print("Contact Added")

    elif ch == 2:
        print(contacts)

    elif ch == 3:
        name = input("Enter name: ")
        if name in contacts:
            print("Number =", contacts[name])
        else:
            print("Contact not found")

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")