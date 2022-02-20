arr = [55, 7, 78, 12, 42]
N = len(arr)

for i in range(N-1, 0, -1):         # 구간의 끝이 변경된다.
    for j in range(0, i):           # 구간의 끝보다 하나 앞자리 요소까지가 기준이 된다.
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
print(arr)