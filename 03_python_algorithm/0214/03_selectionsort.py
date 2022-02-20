arr = [2, 3, 51, 34, 10, 9]
N = 6
for i in range(N-1):
    minidx = i
    for j in range(i+1, N):
        if arr[j] < arr[minidx]:
            minidx = j
    arr[i], arr[minidx] = arr[minidx], arr[i]

print(arr)