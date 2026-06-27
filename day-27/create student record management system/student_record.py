students = {}

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        students[roll] = {"Name": name, "Marks": marks}
        print("Student Record Added Successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No Records Found!")
        else:
            print("\nStudent Records:")
            for roll, data in students.items():
                print("Roll No:", roll)
                print("Name:", data["Name"])
                print("Marks:", data["Marks"])
                print("-------------------")

    elif choice == 3:
        roll = input("Enter Roll Number to Search: ")
        if roll in students:
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student Not Found!")

    elif choice == 4:
        roll = input("Enter Roll Number to Delete: ")
        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == 5:
        roll = input("Enter Roll Number to Update: ")
        if roll in students:
            name = input("Enter New Name: ")
            marks = input("Enter New Marks: ")
            students[roll] = {"Name": name, "Marks": marks}
            print("Record Updated Successfully!")
        else:
            print("Student Not Found!")

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")