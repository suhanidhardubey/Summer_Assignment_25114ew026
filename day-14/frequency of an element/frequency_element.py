n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

x = int(input("Enter element whose frequency you want to find: "))

count = 0

for i in arr:
    if i == x:
        count += 1

print("Frequency of", x, "is", count)