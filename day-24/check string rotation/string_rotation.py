s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")