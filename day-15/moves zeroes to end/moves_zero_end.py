n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

result = []

for i in arr:
    if i != 0:
        result.append(i)

# Count zeroes and add them at the end
zero_count = n - len(result)

for i in range(zero_count):
    result.append(0)

print("Array after moving zeroes to end:")
for i in result:
    print(i, end=" ")