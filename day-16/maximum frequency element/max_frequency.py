arr = [1, 2, 2, 3, 4, 2, 3, 3, 3]

max_freq = 0
max_element = None

for i in arr:
    freq = arr.count(i)
    
    if freq > max_freq:
        max_freq = freq
        max_element = i

print("Element with Maximum Frequency =", max_element)
print("Frequency =", max_freq)