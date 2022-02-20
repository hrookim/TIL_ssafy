arr = [1, 2, 3, 4]
bit = [0]*4

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                for m in range(4):
                    if bit[m]:
                        print(arr[m], end=' ')
                print()