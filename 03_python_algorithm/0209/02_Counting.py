arr = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0]*(len(arr)+1)
Temp = [0]*len(arr)

for number in arr:
    counts[number] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

for number in arr[::-1]:
    counts[number] -= 1
    Temp[counts[number]] = number
    
print(Temp)