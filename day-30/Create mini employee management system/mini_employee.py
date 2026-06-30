emp_id = []
emp_name = []

while True:
    print("\n1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        emp_id.append(input("Enter Employee ID: "))
        emp_name.append(input("Enter Employee Name: "))
        print("Employee Added")

    elif ch == 2:
        print("\nID\tName")
        for i in range(len(emp_id)):
            print(emp_id[i], "\t", emp_name[i])

    elif ch == 3:
        x = input("Enter Employee ID: ")
        if x in emp_id:
            i = emp_id.index(x)
            print("Employee Name:", emp_name[i])
        else:
            print("Employee Not Found")

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")