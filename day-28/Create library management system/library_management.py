books = []

while True:
    print("\n1.Add Book")
    print("2.View Books")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        b = input("Enter book name: ")
        books.append(b)
        print("Book Added")

    elif ch == 2:
        print("Books:", books)

    elif ch == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")