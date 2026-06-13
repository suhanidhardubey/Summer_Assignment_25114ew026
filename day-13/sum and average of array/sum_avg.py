n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Calculate sum
total = 0
for i in arr:
    total += i

# Calculate average
avg = total / n

print("Sum =", total)
print("Average =", avg)