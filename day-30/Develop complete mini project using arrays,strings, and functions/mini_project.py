name = []
roll = []

def add():
    r = input("Enter Roll: ")
    n = input("Enter Name: ")
    roll.append(r)
    name.append(n)
    print("Record Added")

def show():
    print("\nRoll\tName")
    for i in range(len(name)):
        print(roll[i], "\t", name[i])

def search():
    r = input("Enter Roll: ")
    if r in roll:
        i = roll.index(r)
        print("Name:", name[i])
    else:
        print("Record Not Found")

def delete():
    r = input("Enter Roll: ")
    if r in roll:
        i = roll.index(r)
        roll.pop(i)
        name.pop(i)
        print("Record Deleted")
    else:
        print("Record Not Found")

while True:
    print("\n1.Add")
    print("2.Show")
    print("3.Search")
    print("4.Delete")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add()
    elif ch == 2:
        show()
    elif ch == 3:
        search()
    elif ch == 4:
        delete()
    elif ch == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")