tickets = 10

while True:
    print("\n1.Book Ticket")
    print("2.Check Available Tickets")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("How many tickets do you want? "))

        if n <= tickets:
            tickets = tickets - n
            print("Ticket Booked Successfully")
        else:
            print("Tickets not available")

    elif ch == 2:
        print("Available Tickets =", tickets)

    elif ch == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")