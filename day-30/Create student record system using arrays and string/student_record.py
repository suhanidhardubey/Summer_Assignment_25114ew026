name = []
roll = []

while True:
    print("\n1.Add  2.Show  3.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        roll.append(input("Enter Roll: "))
        name.append(input("Enter Name: "))
        print("Record Added")

    elif ch == 2:
        print("\nRoll\tName")
        for i in range(len(name)):
            print(roll[i], "\t", name[i])

    elif ch == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")