employees = {}

while True:
    print("\n--- Salary Management System ---")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))

        hra = 0.20 * basic
        da = 0.10 * basic
        gross_salary = basic + hra + da

        employees[emp_id] = {
            "Name": name,
            "Basic Salary": basic,
            "HRA": hra,
            "DA": da,
            "Gross Salary": gross_salary
        }

        print("Employee Record Added Successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No Records Found!")
        else:
            print("\nEmployee Records:")
            for emp_id, data in employees.items():
                print("Employee ID:", emp_id)
                print("Name:", data["Name"])
                print("Basic Salary:", data["Basic Salary"])
                print("HRA:", data["HRA"])
                print("DA:", data["DA"])
                print("Gross Salary:", data["Gross Salary"])
                print("----------------------")

    elif choice == 3:
        emp_id = input("Enter Employee ID to Search: ")
        if emp_id in employees:
            print("Name:", employees[emp_id]["Name"])
            print("Basic Salary:", employees[emp_id]["Basic Salary"])
            print("HRA:", employees[emp_id]["HRA"])
            print("DA:", employees[emp_id]["DA"])
            print("Gross Salary:", employees[emp_id]["Gross Salary"])
        else:
            print("Employee Not Found!")

    elif choice == 4:
        emp_id = input("Enter Employee ID to Delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Record Deleted Successfully!")
        else:
            print("Employee Not Found!")

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")