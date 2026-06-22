s = input("Enter a string: ")
ch = input("Enter the character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Frequency of", ch, "=", count)