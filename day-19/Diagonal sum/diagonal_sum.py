n = int(input("Enter size of square matrix: "))

A = []
print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

sum_diag = 0

for i in range(n):
    sum_diag += A[i][i]

print("Diagonal Sum =", sum_diag)