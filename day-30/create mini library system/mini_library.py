books = []

while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        b = input("Enter Book Name: ")
        books.append(b)
        print("Book Added")

    elif ch == 2:
        print("Books in Library:")
        for i in books:
            print(i)

    elif ch == 3:
        b = input("Enter Book Name: ")
        if b in books:
            print("Book Available")
        else:
            print("Book Not Available")

    elif ch == 4:
        b = input("Enter Book Name: ")
        if b in books:
            books.remove(b)
            print("Book Issued")
        else:
            print("Book Not Found")

    elif ch == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")