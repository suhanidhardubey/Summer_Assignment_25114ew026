n = int(input("enter a number:"))
count=0

while n:
    count += n & 1
    n >>= 1

print("set bits =",count)    