# 금액 2진수, 3진수 형태로 기억 -> 지금은 각각 한 자리만을 잘못 기억하고 있다.
import sys
sys.stdin = open('input.txt')


def find_same_value(binums, trinums):
    bi_opp = [1, 0]
    for i in range(len(binums)):
        binums[i] = str(bi_opp[int(binums[i])])
        tmp_bi = int(''.join(binums), 2)
        for j in range(len(trinums)):
            trinums[j] = str((int(trinums[j])+1) % 3)
            tmp_tri = int(''.join(trinums), 3)
            if tmp_bi == tmp_tri:
                return tmp_bi
            trinums[j] = str((int(trinums[j])+1) % 3)
            tmp_tri = int(''.join(trinums), 3)
            if tmp_bi == tmp_tri:
                return tmp_bi
            trinums[j] = str((int(trinums[j]) + 1) % 3)
        binums[i] = str(bi_opp[int(binums[i])])
    
    
T = int(input())
for tc in range(1, T+1):
    binums = list(input())
    trinums = list(input())
    
    ans = find_same_value(binums, trinums)
    print(f'#{tc} {ans}')
    
    