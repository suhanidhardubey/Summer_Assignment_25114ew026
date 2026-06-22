s = input("Enter a string: ")

new_str = ""

for ch in s:
    if ch != " ":
        new_str += ch

print("String after removing spaces:", new_str)