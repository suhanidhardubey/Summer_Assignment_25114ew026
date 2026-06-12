def perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

num = int(input("Enter a number: "))

if perfect_number(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")