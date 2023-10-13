import sys
input  = sys.stdin.readline
n= int(input())
lst = list(map(int, input().split()))

tree = [[]for _ in range(n)]


def dfs(lst, l):
    mid = (len(lst)//2)
    tree[l].append(lst[mid])
    if len(lst)==1:
        return
    dfs(lst[:mid], l+1)
    dfs(lst[mid+1:],l+1)
    
dfs(lst,0)

for ele in tree:
    print(*ele)