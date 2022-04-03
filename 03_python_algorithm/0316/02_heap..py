"""
최대 100개의 정수
최대힙
"""
# 1. 삽입 연산
def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    # 부모가 있으면서, 자식의 키값이 더 크면
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


# 2. 삭제 연산
def deq():
    global last
    # 1) 루트의 키 값을 잠시 저장
    tmp = tree[1]
    # 2) 마지막 정점의 값을 루트에 복사
    tree[1] = tree[last]
    # 3) 인덱스로 마지막 정점을 없앤 과정을 한 것이다.
    last -= 1
    # 4) 부모 > 자식 규칙 유지 위해서 자리 바꾸기
    p = 1
    c = 2*p
    
    # 왼쪽 자식이 있으면
    while c <= last:
        # 오른쪽 자식도 있고 더 크면
        if c+1 <= last and tree[c+1] > tree[c]:
            c += 1      # 오른쪽 자식 선택
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    # pop 처럼 꺼내서 반환하는 효과
    return tmp
    

# 포화이진트리의 정점번호:1~100
tree = [0] * 101
last = 0            # 마지막 정점 번호, 아직은 비어있으니까 이렇게 생김

arr = [3, 2, 4, 7, 5, 1]
for k in arr:
    enq(k)
print(tree[1])
enq(9)
print(tree[1])
while last > 0:
    print(deq(), tree[1])
# 이게 바로 heap sort.... 세상에