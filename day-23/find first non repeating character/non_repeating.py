s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found")