def armstrong(num):
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

n = int(input("Enter a number: "))
armstrong(n)