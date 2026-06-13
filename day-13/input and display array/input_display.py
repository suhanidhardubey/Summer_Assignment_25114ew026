n = int(input("Enter number of elements: "))

# Create array (list)
arr = []

# Input elements
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Display array
print("Array elements are:")
for i in arr:
    print(i, end=" ")