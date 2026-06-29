s = input("Enter a string: ")

while True:
    print("\n--- String Menu ---")
    print("1. Length of String")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Reverse String")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("Length =", len(s))

    elif ch == 2:
        print("Uppercase =", s.upper())

    elif ch == 3:
        print("Lowercase =", s.lower())

    elif ch == 4:
        print("Reverse =", s[::-1])

    elif ch == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")