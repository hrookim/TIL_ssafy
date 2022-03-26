'''
4
1 2 1 3 3 4 3 5
'''
def preorder(V):
    if V:
        print(V, end="-> ")
        preorder(ch1[V])
        preorder(ch2[V])
        

def inorder(V):
    if V:
        preorder(ch1[V])
        print(V, end="-> ")
        preorder(ch2[V])


def postorder(V):
    if V:
        preorder(ch1[V])
        preorder(ch2[V])
        print(V, end="-> ")

    
E = int(input())        # 간선의 수
arr = list(map(int, input().split()))
V = E+1                 # 정점의 수 == 1번부터 V번까지 정점이 있을 때 마지막 정점

# 1. 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    elif ch1[p]:
        ch2[p] = c

# print(ch1, ch2, sep="\n")
# preorder(1)
# print()
# inorder(1)
# print()
# postorder(1)

'''
4 
2 1 2 4 4 3 4 5
'''
# 2. 자식을 인덱스로 부모 번호 저장 -> 루트 찾기 / 조상 찾기 가능!
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
print(par)

# 2-1. root찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0:
        root = i
        break
print(root)

# 2-2. 조상찾기
c = 5
anc = []
while par[c]:
    anc.append(par[c])
    c = par[c]
print(*anc)