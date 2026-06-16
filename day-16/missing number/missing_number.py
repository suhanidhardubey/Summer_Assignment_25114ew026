arr = [1, 2, 3, 5]
n = 5

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum

print("Missing Number =", missing)