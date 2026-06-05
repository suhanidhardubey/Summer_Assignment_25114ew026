n = int (input("enter a number;"))
largest = 0

i=2
while i<= n:
    if n% i==0:
        largest =i
        n//=i
    else:
        i+=1

print("largest prime factor =",largest)
            