rows = 4

for i in range(2, rows + 2):
    # Print spaces
    for j in range(rows - i + 1):
        print(" ", end="")

    # Print ascending numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Print descending numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()