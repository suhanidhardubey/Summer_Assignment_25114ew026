n = int(input("enter a number:"))
count = 0
while n > 0:
    count += n & 1
    n = n>>1
print("number of set bits:",count)
    