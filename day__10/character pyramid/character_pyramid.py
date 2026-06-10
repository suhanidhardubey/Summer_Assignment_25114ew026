rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    ch = 'A'
    for j in range(2 * i + 1):
        print(ch, end="")
        ch = chr(ord(ch) + 1)

    print()