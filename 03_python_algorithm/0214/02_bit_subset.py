arr = [1, 2, 3]

n = len(arr)
result = []

for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    result.append(subset)
print(result)