n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

# Reverse the array
arr.reverse()

print("Reversed array:")
for i in arr:
    print(i, end=" ")