arr = [1, 2, 3]
for i1 in range(1, 3+1):
    for i2 in range(1, 3+1):
        if i1 != i2:
            for i3 in range(1, 3+1):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)